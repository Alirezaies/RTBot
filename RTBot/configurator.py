from typing import Callable


class Configurator:
    def __init__(self) -> None:
        """ Configurator: used to return configuration values """

        self.version = '0.0.0'
        self.uid = None
        self.cuid = None

    def info_processor(
        self,
        args: list,
        parser: Callable
    ) -> None:
        """ process the info subcommand """

        if(args.version):
            print('Version: ' + self.version)
        else:
            parser(['info', '--help'])

    def run_bot_processor(
        self,
        args: list,
        parser: Callable
    ) -> None:
        """ process the run-bot command """

        if args.userid and args.channelid:
            self.uid = args.userid
            self.cuid = args.channelid
        else:
            parser(['run-bot', '--help'])

    def get_version(self) -> str:
        """ get the programm version """
        return(self.version)

    def get_uid(self) -> int:
        """ get the admin userid """
        return(str(self.uid))

    def get_cuid(self) -> str:
        """ get the channel id """
        return(self.cuid)
