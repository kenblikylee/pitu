from abc import ABC, abstractmethod
from .photo import Photo, EmptyPhoto

class PinStyleABC(ABC):
    def __init__(self, *photos):
        self._photos = photos
    @abstractmethod
    def pin(self):
        pass

class PinStyleX(PinStyleABC):
    def pin(self, color='white'):
        photos = self._photos
        # print('PinStyleX: {0!r}'.format(photos))
        w = sum([photo.size()[0] for photo in photos])
        h = max([photo.size()[1] for photo in photos])
        canvas = EmptyPhoto(w, h, color)
        x, y = 0, 0
        for photo in photos:
            canvas.paste(photo, x, y)
            x += photo.size()[0]
        return canvas

class PinStyleY(PinStyleABC):
    def pin(self, color='white'):
        photos = self._photos
        # print('PinStyleY: {0!r}'.format(self._photos))
        w = max([photo.size()[0] for photo in photos])
        h = sum([photo.size()[1] for photo in photos])
        canvas = EmptyPhoto(w, h, color)
        x, y = 0, 0
        for photo in photos:
            canvas.paste(photo, x, y)
            y += photo.size()[1]
        return canvas
