from abc import ABC, abstractmethod
from .photo import Photo, EmptyPhoto

class PinStyleABC(ABC):
    def __init__(self, *photos):
        self._photos = photos
    @abstractmethod
    def pin(self):
        pass

class PinStyleX(PinStyleABC):
    def pin(self, color='white', same=False):
        photos = self._photos
        if same:
            h_same = min([photo.size()[1] for photo in photos])
            for photo in photos:
                photo.zoom(height=h_same)
            w = sum([photo.size()[0] for photo in photos])
            h = h_same
        else:
            w = sum([photo.size()[0] for photo in photos])
            h = max([photo.size()[1] for photo in photos])
        canvas = EmptyPhoto(w, h, color)
        x, y = 0, 0
        for photo in photos:
            canvas.paste(photo, x, y)
            x += photo.size()[0]
        return canvas

class PinStyleY(PinStyleABC):
    def pin(self, color='white', same=False):
        photos = self._photos
        if same:
            w_same = min([photo.size()[0] for photo in photos])
            for photo in photos:
                photo.zoom(width=w_same)
            w = w_same
            h = sum([photo.size()[1] for photo in photos])
        else:
            w = max([photo.size()[0] for photo in photos])
            h = sum([photo.size()[1] for photo in photos])
        canvas = EmptyPhoto(w, h, color)
        x, y = 0, 0
        for photo in photos:
            canvas.paste(photo, x, y)
            y += photo.size()[1]
        return canvas

class PinStyleGrid(PinStyleABC):
    def __init__(self, *photos, rows=3, cols=3, width=300, height=300):
        super().__init__(*photos)
        self._rows = rows
        self._cols = cols
        self._width = width
        self._height = height
        self._num = rows * cols
        if len(self._photos) > self._num: self._photos = self._photos[:self._num]
    def pin(self, color='white', gap=0, padding=0):
        rows, cols, width, height = self._rows, self._cols, self._width, self._height
        photos = self._photos
        photos_num = len(photos)
        canvas = EmptyPhoto(width, height, color)
        cell_w = int((width - 2*padding - (cols-1)*gap)/cols)
        cell_h = int((height - 2*padding - (rows-1)*gap)/rows)
        from .utils import centerratio
        for photo in photos:
            _w, _h = _size = photo.size()
            _center = int(_w/2), int(_h/2)
            photo.cut(*centerratio(_size, _center, ratio=cell_w/cell_h))
            photo.zoom(width=cell_w)

        k = 0
        x = y = padding
        cell_ww = cell_w + gap
        cell_hh = cell_h + gap
        for i in range(rows):
            if k >= photos_num: break
            # 垂直边缘对齐处理
            if i > 0 and (i == rows-1):
                y = height - cell_h - padding
            for j in range(cols):
                # 水平边缘对齐处理
                if j > 0 and (j == cols-1):
                    x = width - cell_w - padding
                canvas.paste(photos[k], x, y)
                k += 1
                if k >= photos_num: break
                x += cell_ww
            x = padding
            y += cell_hh
        return canvas
