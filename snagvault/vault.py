from getpass import getpass

import keyring


class __Vault(object):
    class KeyError(Exception):
        pass

    def __init__(self):
        self.service = 'Snag Vault'

    def __setitem__(self, key, item):
        self.set_password(key, item)

    def __getitem__(self, key, prompt_on_error=False):
        try:
            value = self.get_password(key)
        except vault.KeyError:
            if prompt_on_error:
                value = self.set_password_by_input(
                    key,
                    msg='Please input passphrase',
                    hidden=True)
            else:
                raise vault.KeyError
        return value

    def get_password(self, key):
        value = keyring.get_password(self.service, key)
        if value is None:
            raise vault.KeyError(self.service, key)
        return value

    def set_password(self, key, password):
        keyring.set_password(self.service, key, password)

    def set_password_by_input(self, key, msg=None, hidden=True):
        password = None
        confirm = None
        if not msg:
            msg = 'Please Enter in a value for {}: '.format(key)

        while (password != confirm) or (password is None):
            if hidden:
                password = getpass(prompt=msg)
                confirm = getpass('Please confirm: ')
            else:
                password = input(msg)
                confirm = password
            self.set_password(key, password)
        return password


vault = __Vault()
