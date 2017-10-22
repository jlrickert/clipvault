import random

import pyperclip
from termcolor import colored, cprint

from rfc3987 import parse

from .cli import AbstractCli


class SnagCli(AbstractCli):
    """Snag description

    """
    name = 'snag'

    def random_password(length):
        return ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyz' +
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
            '1234567890' +
            '!@#$%^&*()') for i in range(length))

    def command(self, args):
        key = self.__process_key(args.key)
        value, text = self.__fetch_value(key)
        pyperclip.copy(value)
        cprint(text)

    def _setup_parser(self, parser):
        parser.add_argument(
            'key', nargs='?', type=str,
            help='key to fetch from vault')

    def __process_key(self, key):
        if key is None:
            key = pyperclip.paste()
        try:
            uri = parse(key)
            key = uri['authority']
        except ValueError:
            pass
        return key

    def __fetch_value(self, key):
        try:
            value = self.vault[key]
            text = colored('"{} copied to clipboard!"'.format(
                key), 'green')
        except self.vault.KeyError:
            value = SnagCli.random_password(16)
            text = colored(
                '"Generated random value for {}"'.format(key),
                'red')
        return value, text
