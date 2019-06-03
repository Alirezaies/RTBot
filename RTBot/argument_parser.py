import argparse
import sys

from  RTBot import configurator

# Parser:<Class>: Command Line Argument Parser
class Parser:
    def __init__(self):
        self.configurator = configurator.Configurator()
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

        self.info_parser.set_defaults(func=self.configurator.info_processor)
        self.run_parser.set_defaults(func=self.configurator.run_bot_processor)

    
    def __declare_args(self):
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
        self.__declare_args()
        if len(sys.argv) == 1:
            self.parser.parse_args(['--help'])
        else:
            args = self.parser.parse_args()
            args.func(args, self.parser.parse_args)