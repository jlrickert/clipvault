import os
import sys

from ..vault import vault as vault_
from .cli import AbstractCli


class VaultCli(AbstractCli):
    """Vault description
    """
    name = 'vault'


def vault():
    args = sys.argv
    cli = VaultCli(args, vault_)
    return cli.run()


if __name__ == '__main__':
    os.exit(vault())
