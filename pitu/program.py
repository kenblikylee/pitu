from . import zoom, rotate, flip, cut, gray, text, avatar, cover, pin, grid
from os import path
import re

def exec(program_file):
    if not path.isfile(program_file):
        print('no such program file: {}'.format(program_file))
        return
    print('execute program file {}'.format(program_file))

    with open(program_file) as f:
        for line in f:
            line = line.strip()
            if line != '':
                print(line)
                argv = cliparse(line)
                cmd, params = argv[0], argv[1:]
                if cmd == 'zoom':
                    zoom.zoom(params[0], params[1:])
                elif cmd == 'rotate':
                    rotate.rotate(params[0], params[1:])
                elif cmd == 'flip':
                    flip.flip(params[0], params[1:])
                elif cmd == 'cut':
                    cut.cut(params[0], params[1:])
                elif cmd == 'gray':
                    gray.gray(params[0], params[1:])
                elif cmd == 'text':
                    text.text(params[0], params[1:])
                elif cmd == 'avatar':
                    avatar.avatar(params[0], params[1:])
                elif cmd == 'cover':
                    cover.cover(params[0], params[1:])
                elif cmd == 'pin':
                    pin.pin(params)
                elif cmd == 'grid':
                    grid.grid(params)

def cliparse(line):
    r = re.findall(r'(([\'\"]).*?\2)', line)
    s = []
    if r is None:
        s = re.split(r'\s+', line)
    elif isinstance(r, list):
        for item in r:
            ms = item[0]
            tmp =  re.split(r'\s*{}\s*'.format(ms), line)
            tmp0 = tmp[0].strip()
            if tmp0 != '':
                s += re.split(r'\s+', tmp0)
            s.append(ms.strip('\'|\"'))
            line = tmp[1].strip()
        if line != '':
            s += re.split(r'\s+', line)
    return s
