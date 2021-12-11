import sys


def readfile(path):
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    return lines


args = sys.argv[1:]

if not sys.stdin.isatty():
    lines = sys.stdin.readlines()
elif len(args) > 0:
    lines = readfile(args[0])
    args = args[1:]

lines = [line.replace('\n', '') for line in lines]

data = '\n'.join(lines)
