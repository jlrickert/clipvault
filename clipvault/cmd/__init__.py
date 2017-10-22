import sys

from ..vault import vault as vault_
from .snag import SnagCli
from .vault import VaultCli


def snag():
    args = sys.argv
    cli = SnagCli(args, vault_)
    sys.exit(cli.run())


def vault():
    args = sys.argv
    cli = VaultCli(args, vault_)
    sys.exit(cli.run())
