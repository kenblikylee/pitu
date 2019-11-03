from . import *
from . import __version__

def main():
    try:
        ap = _argparse()
    except Exception as exp:
        print(exp)
        exit(1)
    cmd, cmdparams, photo, params = ap['cmd'], ap['cmdparams'], ap['photo'], ap['params']

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
    elif cmd == 'grid':
        grid.grid(cmdparams)

def _argparse():
    import sys as _sys
    argv, arg_len = _sys.argv, len(_sys.argv)
    if arg_len < 2 or (argv[1] == '-v'):
        print('pitu v{}'.format(__version__))
        exit(0)
    if arg_len < 3: raise Exception('Usage: pitu cmd xxx ...')

    cmd = argv[1]

    return dict(cmd = argv[1],
                cmdparams = argv[2:],
                photo = argv[2],
                params = (argv[3:] if arg_len > 3 else None))
