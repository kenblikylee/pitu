from .photo import Photo

def zoom(photo, params, show=False):
    _photo = Photo(photo).zoom(**_parse(params))
    _photo.save('zoom-' + photo)
    if show: _photo.show()

def _parse(params):
    _len = len(params)
    return dict(ratio = (float(params[0]) if _len > 0 else None),
                width = (int(params[1]) if _len > 1 else None),
                height = (int(params[2]) if _len > 2 else None))
