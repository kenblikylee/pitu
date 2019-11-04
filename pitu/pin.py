from .photo import Photo
from .pinstyle import PinStyleX, PinStyleY

def pin(params, show=False, same=True):
    axis, photos = params[0], params[1:]
    if photos[-1] == 'diff':
        same = False
        photos = photos[:-1]
    photos = [Photo(photo) for photo in photos]
    if axis == 'x':
        _photo = PinStyleX(*photos).pin(same=same)
    elif axis == 'y':
        _photo = PinStyleY(*photos).pin(same=same)
    else:
        return
    _photo.save('pin-photos.png')
    if show: _photo.show()
