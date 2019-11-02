from .photo import Photo

def flip(photo, params, show=False):
    _photo = Photo(photo).flip(**_parse(params))
    _photo.save('flip-' + photo)
    if show: _photo.show()

def _parse(params):
    _len = len(params)
    return dict(axis = (str(params[0]) if _len > 0 else None))
