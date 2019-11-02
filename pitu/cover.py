from .photo import Photo, EmptyPhoto
from .utils import centerratio, expandratio

def cover(photo, params, show=False):
    _photo = Photo(photo)
    _p = _parse(params)
    _ratio = _p['ratio']
    if _p['mode'] == 'ex':
        w, h, x, y = expandratio(_photo.size(), _ratio)
        _photo = EmptyPhoto(width=w, height=h).paste(_photo, x, y)
    else:
        _w, _h = _size = _photo.size()
        _center = int(_w/2), int(_h/2)
        _photo.cut(*centerratio(_size, _center, _ratio))

    _photo.save('cover-' + photo)
    if show: _photo.show()

def _parse(params):
    if params is None:
        return dict(mode = 'ce', ratio = '4:3')
    _len = len(params)
    return dict(mode = (str(params[0]) if _len > 0 else 'ce'),
                ratio = (str(params[1]) if _len > 1 else '4:3'))
