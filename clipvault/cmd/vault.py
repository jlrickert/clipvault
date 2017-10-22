import pyperclip
from termcolor import colored, cprint

from rfc3987 import parse

from .cli import AbstractCli


class VaultCli(AbstractCli):
    """Vault description

    """
    name = 'vault'

    def command(self, args):
        key, fromCb = self.__process_key(args.key)
        if key and not fromCb:
            value = pyperclip.paste()
            self.vault[key] = value
        else:
            value = self.vault.set_password_by_input(key)

        pyperclip.copy(value)
        text = colored(
            'Value for {} has been set and is now in your clipboard!'.format(
                key),
            'green')
        cprint(text)

    def _setup_parser(self, parser):
        parser.add_argument(
            'key', nargs='?', type=str,
            help='Key to store contents of clipboard into')

    def __process_key(self, key):
        fromCb = False
        if key is None:
            key = pyperclip.paste()
            fromCb = True
        try:
            tmp_key = key
            uri = parse(tmp_key)
            if uri['authority'] is not None:
                key = uri['authority']
        except ValueError:
            pass
        return key, fromCb

    def __process_value(self):
        return pyperclip.paste(), True
