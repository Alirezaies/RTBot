import argparse

# Parser:<Class>: Command Line Argument Parser
class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(add_help=True)
        self.subparser = self.parser.add_subparsers(
            title='subcommands',
            help='sub-commands help'
        )
        self.info_parser = self.subparser.add_parser(
            'info',
            help='getting programm info'
        )
        self.run_parser = self.subparser.add_parser(
            'run-bot',
            help='run command and arguments'
        )
    
    def declare_args(self):
        # Declaring Arguments
        self.info_parser.add_argument(
            '-v',
            '--version',
            action='store_true',
            dest='version',
            default=False,
            help='prints the version of the programm'
        )

        self.run_parser.add_argument(
            '-uid',
            '--userid',
            metavar='<USERID>',
            nargs='?',
            dest='userid',
            help='userid input for the master admin',
            required=True
        )

        self.run_parser.add_argument(
            '-cuid',
            '--channeluid',
            metavar='<CHANNELUID>',
            nargs='?',
            dest='channelid',
            help='channel username',
            required=True
        )

    def parse(self):
        self.parser.parse_args()