from .photo import Photo
from .pinstyle import PinStyleGrid

def grid(params, show=False):
    _params, _photos = _parse(params)
    photos = [Photo(photo) for photo in _photos]
    if _params is None:
        _photo = PinStyleGrid(*photos).pin()
    else:
        _rcwh = dict()
        for _key in ['rows', 'cols', 'width', 'height']:
            if _key in _params: _rcwh[_key] = int(_params[_key])
        _cgp = dict()
        for _key in ['color', 'gap', 'padding']:
            if _key in _params:
                if _key == 'color': _cgp[_key] = _params[_key] 
                else: _cgp[_key] = int(_params[_key])

        _photo = PinStyleGrid(*photos, **_rcwh).pin(**_cgp)
    _photo.save('grid-photos.png')
    if show: _photo.show()

def _parse(params):
    first = params[0]
    last = params[-1]
    if first[0] == ':':
        _params = [p.strip(':| ') for p in first.split(' ')]
        _params = {p.split('=')[0]: p.split('=')[1] \
                    for p in _params}
        _photos = params[1:]
    elif last[0] == ':':
        _params = [p.strip(':| ') for p in last.split(' ')]
        _params = {p.split('=')[0]: p.split('=')[1] \
                    for p in _params}
        _photos = params[:-1]
    else:
        _params = None
        _photos = params
    return _params, _photos
