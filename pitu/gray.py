from .photo import Photo

def gray(photo, params, show=False):
    _photo = Photo(photo).gray()
    _photo.save('gray-' + photo)
    if show: _photo.show()
