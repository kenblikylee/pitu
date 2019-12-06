from .photo import Photo, EmptyPhoto
from .utils import centerratio, expandratio

def avatar(photo, params, show=False):
    _photo = Photo(photo)
    _params = _parse(params)
    if _params['mode'] == 'ex':
        w, h, x, y = expandratio(_photo.size())
        _photo = EmptyPhoto(width=w, height=h, bgcolor=_params['bgcolor']).paste(_photo, x, y)
    else:
        _w, _h = _size = _photo.size()
        _center = int(_w/2), int(_h/2)
        _photo.cut(*centerratio(_size, _center))

    _photo.save('avatar-' + photo)
    if show: _photo.show()

def _parse(params):
    if params is None:
        return dict(mode = 'ce', bgcolor = 'white')
    _len = len(params)
    return dict(mode = (str(params[0]) if _len > 0 else None),
                bgcolor = (str(params[1]) if _len > 1 else 'white'))
