import os
import sys

from ..vault import vault
from .cli import AbstractCli


class SnagCli(AbstractCli):
    """Snag description
    """
    name = 'snag'


def snag():
    args = sys.argv
    cli = SnagCli(args, vault)
    return cli.run()


if __name__ == '__main__':
    os.exit(snag())
