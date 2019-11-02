from .photo import Photo, EmptyPhoto
from .utils import centerratio, expandratio

def avatar(photo, params, show=False):
    _photo = Photo(photo)
    if _parse(params)['mode'] == 'ex':
        w, h, x, y = expandratio(_photo.size())
        _photo = EmptyPhoto(width=w, height=h).paste(_photo, x, y)
    else:
        _w, _h = _size = _photo.size()
        _center = int(_w/2), int(_h/2)
        _photo.cut(*centerratio(_size, _center))

    _photo.save('avatar-' + photo)
    if show: _photo.show()

def _parse(params):
    if params is None:
        return dict(mode = 'ce')
    _len = len(params)
    return dict(mode = (str(params[0]) if _len > 0 else None))
