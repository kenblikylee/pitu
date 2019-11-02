from .photo import Photo
from .pinstyle import PinStyleX, PinStyleY

def pin(axis, photos, show=False):
    photos = [Photo(photo) for photo in photos]
    if axis == 'x':
        _photo = PinStyleX(*photos).pin()
    elif axis == 'y':
        _photo = PinStyleY(*photos).pin()
    else:
        return
    _photo.save('pin-photos.png')
    if show: _photo.show()
