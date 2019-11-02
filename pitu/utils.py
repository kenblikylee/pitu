def _get_ratio(ratio):
    if isinstance(ratio, str):
        if ':' in ratio:
            r_w, r_h = ratio.split(':')
            try:
                ratio = float(r_w) / float(r_h)
            except:
                raise
    if not isinstance(ratio, float):
        ratio = float(ratio)
    return ratio

def centerratio(size, center, ratio=1.0):
    def _calc_max_size(size, center):
        w, h = size
        x_l, y_t = center
        x_r, y_b = w-x_l, h-y_t
        return min(x_l, x_r)*2, min(y_t, y_b)*2

    ratio = _get_ratio(ratio)
    width_max, height_max = _calc_max_size(size, center)
    width_ratio = round(height_max * ratio)
    width = min(width_max, width_ratio)
    height = round(width / ratio)

    return center[0] - round(width/2), \
           center[1] - round(height/2), \
           width, height

def expandratio(size, ratio=1.0):
    ratio = _get_ratio(ratio)
    w, h = size
    w_r = round(h * ratio)
    if w > w_r:
        h_r = round(w / ratio)
        return w, h_r, 0, int((h_r-h)/2)
    elif w < w_r:
        return w_r, h, int((w_r-w)/2), 0
    else:
        return w, h, 0, 0
