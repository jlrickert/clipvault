import sys

import pyperclip
from termcolor import colored, cprint

from .vault import vault


def usage():
    print('Missing key')


def copy_key(key, timeout=5):
    try:
        value = vault[key]
        pyperclip.copy(value)
        text = colored(
            '"{} copied to clipboard for {} minutes!"'.format(key, timeout),
            'green')
    except vault.KeyError:
        text = colored(
            '"{} has no associated value"'.format(key, timeout),
            'red')
    cprint(text)


def set_key(key, value):
    vault[key] = value


def main() -> None:
    args = sys.argv
    if len(args) == 2:
        copy_key(args[1])
    elif len(args) >= 3:
        set_key(args[1], args[2])
    else:
        usage()


if __name__ == '__main__':
    sys.exit(main())
