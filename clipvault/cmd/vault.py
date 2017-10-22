import pyperclip
from termcolor import colored, cprint

from .cli import AbstractCli


class VaultCli(AbstractCli):
    """Vault description
    """
    name = 'vault'

    def command(self, args):
        key = args.key
        value = pyperclip.paste()
        self.vault[key] = value
        text = colored(
            'Value for {} has been set!'.format(key),
            'green')
        cprint(text)

    def _setup_parser(self, parser):
        parser.add_argument(
            'key',
            type=str,
            help='Key to store contents of clipboard into')
