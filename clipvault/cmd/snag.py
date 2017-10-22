import pyperclip
from termcolor import colored, cprint

from .cli import AbstractCli


class SnagCli(AbstractCli):
    """Snag description

    """
    name = 'snag'

    def command(self, args):
        key = args.key
        try:
            value = self.vault[key]
            pyperclip.copy(value)
            text = colored('"{} copied to clipboard!"'.format(
                key), 'green')
        except self.vault.KeyError:
            text = colored('"{} has no associated value"'.format(key), 'red')
        cprint(text)

    def _setup_parser(self, parser):
        parser.add_argument('key', type=str, help='key to fetch from vault')
