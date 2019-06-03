class Configurator:
    def __init__(self):
        self.version = '0.0.0'
        self.uid = None
        self.cuid = None

    def info_processor(self, args, parser):
        """ process the info subcommand """

        if(args.version):
            print('Version: ' + self.version)
        else:
            parser(['info', '--help'])
    
    def run_bot_processor(self, args, parser):
        """ process the run-bot command """

        if args.userid and args.channelid:
            self.uid = args.userid
            self.cuid = args.channelid
        else:
            parser(['run-bot', '--help'])
    
    def get_version(self):
        """ get the programm version """
        return(self.version)
    
    def get_uid(self):
        """ get the admin userid """
        return(self.uid)

    def get_cuid(self):
        """ get the channel id """
        return(self.cuid)