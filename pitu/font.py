from PIL import ImageFont

PHOTO_FONTS = {
    'pf': 'PingFang.ttc',
    'yh': 'msyh.ttc'
}

def font(font_name, font_size=20):
    if font_name not in PHOTO_FONTS:
        raise Exception('unsupported font: {0}, try one of {1!r}'.format(font_name, PHOTO_FONTS.keys()))
    try:
        font_file = PHOTO_FONTS[font_name]
        _font = ImageFont.truetype(font_file, font_size, encoding='unic')
    except OSError:
        raise Exception('OSError: 系统找不到字体文件 {}'.format(font_file))
    return _font
