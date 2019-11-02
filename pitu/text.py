from .photo import Photo

def text(photo, params, show=False):
    _photo = Photo(photo).text(**_parse(params))
    _photo.save('text-' + photo)
    if show: _photo.show()

def _parse(params):
    _len = len(params)
    return dict(text = (str(params[0]) if _len > 0 else None),
                x = (int(params[1]) if _len > 1 else 0),
                y = (int(params[2]) if _len > 2 else 0),
                font_size = (int(params[3]) if _len > 3 else 20),
                color = (str(params[4]) if _len > 4 else 'black'),
                font_name = (str(params[5]) if _len > 5 else 'pf'))
