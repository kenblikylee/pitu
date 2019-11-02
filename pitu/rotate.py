from .photo import Photo

def rotate(photo, params, show=False):
    _photo = Photo(photo).rotate(**_parse(params))
    _photo.save('rotate-' + photo)
    if show: _photo.show()

def _parse(params):
    _len = len(params)
    return dict(angle = (int(params[0]) if _len > 0 else None),
                fill = (str(params[1]) if _len > 1 else None))
