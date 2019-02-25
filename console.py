import sys
import os
import argparse

def tree(path, mask=''):
    dir = os.listdir(path)
    j = 0
    while j < len(dir):

        if dir[j][0]=='.' and args.all:
            dir.pop(j)

        elif os.path.isfile(os.path.join(path,dir[j])):
            if args.folders_only:
                dir.pop(j)
            elif args.include is not None and dir[j].find(args.include)==-1:
                dir.pop(j)
            elif args.exclude is not None and dir[j].find(args.exclude)!=-1:
                dir.pop(j)
            else:
                j += 1

        else:
            j +=1

    for j in range(len(dir)-1):
        if args.full:
            name = os.path.join(path,dir[j])
        else:
            name = dir[j]

        if args.pretty:
            print(mask, '├─ ', name, sep='')
        else:
            print(mask, '   ', name, sep='')
        if os.path.isdir(os.path.join(path,dir[j])):
            if args.pretty:
                tree(os.path.join(path,dir[j]), mask + '│  ')
            else:
                tree(os.path.join(path,dir[j]), mask + '   ')
    j = len(dir) - 1
    if j < 0:
        return
    if args.full:
        name = os.path.join(path,dir[j])
    else:
        name = dir[j]	
    if args.pretty:
        print(mask, '└─ ', name, sep='')
    else:
        print(mask, '   ', name, sep='')
    if os.path.isdir(os.path.join(path,dir[j])):
        tree(os.path.join(path,dir[j]),mask + '   ')

parser = argparse.ArgumentParser(
    description='Статистика для самых маленьких'
)

parser.add_argument(
    'path',
    metavar='PATH',
    type=str,
    nargs='?',
    default='.',
    help='исходная директория'
)

parser.add_argument(
    '-f',
    '--folders-only',
    action='store_true',
    help='выводить только имена папок'
)

parser.add_argument(
    '-p',
    '--pretty',
    action='store_true',
    help='выводить графические элементы'
)

parser.add_argument(
    '-a',
    '--all',
    action='store_false',
    help='выводить полное дерево'
)

parser.add_argument(
    '-l',
    '--full',
    action='store_true',
    help='выводить полное имя'
)

parser.add_argument(
    '-I',
    '--include',
    metavar='SOME_TEXT',
    type=str,
    action='store',
    help='выводить только имена, содержащие SOME_TEXT'
)

parser.add_argument(
    '-E',
    '--exclude',
    metavar='SOME_TEXT',
    type=str,
    action='store',
    help='не выводить имена, содержащие SOME_TEXT'
)

args = parser.parse_args()

print(args.path)
tree(args.path)
