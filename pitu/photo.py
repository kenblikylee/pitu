from PIL import Image, ImageDraw
from .font import font

class Photo:
    def __init__(self, photo=None, image=None):
        try:
            if isinstance(image, Image.Image):
                self._image = image
            else:
                self._image = Image.open(photo)
        except FileNotFoundError:
            self._image = None
            print('photo {} not found.'.format(photo))
            # raise
        if self._image:
            self._origin = self._image
    def size(self):
        return self._image.size
    def show(self):
        self._image.show()
        return self
    def save(self, save_path):
        self._image.save(save_path)
        return self
    def zoom(self, ratio=None, width=None, height=None):
        w, h = self._image.size
        if height is not None:
            ratio = height / h
        elif width is not None:
            ratio = width / w
        elif ratio is None:
            raise Exception('zoom missing parameter!!!')

        z_w, z_h = round(w * ratio), round(h * ratio)
        self._image = self._image.resize((z_w, z_h))
        return self
    def rotate(self, angle, fill='white'):
        self._image = self._image.rotate(angle, fillcolor=fill)
        return self
    def flip(self, axis='x'):
        if axis == 'x':
            self._image = self._image.transpose(Image.FLIP_LEFT_RIGHT)
        elif axis == 'y':
            self._image = self._image.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            raise Exception('invalid axis parameter.')
        return self
    def cut(self, x, y, width, height):
        self._image = self._image.crop((x, y, x+width, y+height))
        return self
    def gray(self):
        self._image = self._image.convert("L")
        return self
    def text(self, text, x, y, color='black', font_name='pf', font_size=20):
        _font = font(font_name, font_size)
        draw = ImageDraw.Draw(self._image)
        draw.text((x, y), text, fill=color, font=_font)
        return self
    def textsize(self, text, font_name, font_size):
        return font(font_name, font_size).getsize(text)
    def paste(self, photo, x, y):
        self._image.paste(photo._image, (x, y))
        return self

class EmptyPhoto(Photo):
    def __init__(self, width=200, height=100, bgcolor='white'):
        super().__init__(image=Image.new('RGB', (width, height), bgcolor))

class TextPhoto(EmptyPhoto):
    def __init__(self, text='文字图片', color='black', font_name='pf', x_offset=0, y_offset=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        w, h = self.size()
        padding = round(w / 20)
        t_w = w - 2*padding
        word_num = len(text)
        font_size = round(t_w / word_num)
        t_w, t_h = self.textsize(text, font_name, font_size)
        x, y = round((w - t_w)/2), round((h-t_h)/2)
        self.text(text, x+x_offset, y-y_offset, color=color, font_name=font_name, font_size=font_size)
