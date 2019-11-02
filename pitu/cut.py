from .photo import Photo

def cut(photo, params, show=False):
    _photo = Photo(photo).cut(**_parse(params))
    _photo.save('cut-' + photo)
    if show: _photo.show()

def _parse(params):
    _len = len(params)
    return dict(x = (int(params[0]) if _len > 0 else None),
                y = (int(params[1]) if _len > 1 else None),
                width = (int(params[2]) if _len > 2 else None),
                height = (int(params[3]) if _len > 3 else None))
