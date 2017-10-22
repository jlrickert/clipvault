import argparse


class AbstractCli(object):
    """stuff
    """

    def __init__(self, args, vault):
        self.args = args
        self.vault = vault
        self.parser = argparse.ArgumentParser(
            prog=self.name,
            description=self.__doc__)
        # self.subparsers = self.parser.add_subparsers()
        # self.subparsers.dest = 'command'
        # self.subparsers.require = True
        # self.__add_get_parser()
        # self.__add_set_parser()

    def print_usage(self):
        print(self.__doc__)

    def run(self):
        self.parser.parse_args(self.args)

    # def __add_get_parser(self):
    #     get_parser = self.subparsers.add_parser('get')
    #     get_parser.add_argument(
    #         'key',
    #         type=str,
    #         help="Key to fetch from vault")

    # def __add_set_parser(self):
    #     set_parser = self.subparsers.add_parser('set')
    #     set_parser.add_argument()
    #     set_parser.add_argument(
    #         'key',
    #         type=str,
    #         help="Key to place contents of clipboard into vault.")
