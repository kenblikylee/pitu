from . import *

def main():
    try:
        ap = _argparse()
    except Exception as exp:
        print(exp)
        exit(1)
    cmd, photo, params = ap['cmd'], ap['photo'], ap['params']

    if cmd == 'zoom':
        zoom.zoom(photo, params)
    elif cmd == 'rotate':
        rotate.rotate(photo, params)
    elif cmd == 'flip':
        flip.flip(photo, params)
    elif cmd == 'cut':
        cut.cut(photo, params)
    elif cmd == 'gray':
        gray.gray(photo, params)
    elif cmd == 'text':
        text.text(photo, params)
    elif cmd == 'pin':
        pin.pin(photo, params)
    elif cmd == 'avatar':
        avatar.avatar(photo, params)
    elif cmd == 'cover':
        cover.cover(photo, params)

def _argparse():
    import sys as _sys
    argv, arg_len = _sys.argv, len(_sys.argv)
    if arg_len < 3: raise Exception('Usage: pitu cmd photo ...')

    cmd = argv[1]

    return dict(cmd = argv[1],
                photo = argv[2],
                params = (argv[3:] if arg_len > 3 else None))
