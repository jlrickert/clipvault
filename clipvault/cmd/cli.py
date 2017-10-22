import argparse


class AbstractCli(object):
    """AbstractCli

    """

    def __init__(self, args, vault):
        self.args = args
        self.vault = vault
        self.parser = argparse.ArgumentParser(
            prog=self.name,
            description=self.__doc__)

    def print_usage(self):
        print(self.__doc__)

    def _setup_parser(self, parser):
        pass

    def command(self, args):
        pass

    def run(self):
        self._setup_parser(self.parser)
        self.parser.parse_args()
        args = self.parser.parse_args()
        self.command(args)
