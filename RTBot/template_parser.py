import json
import os


class template_parser:
    def __init__(self) -> None:
        """ template_parser class: used to parse and proccess the messages """

        template = (os.path.dirname(
            os.path.realpath(__file__)), 'template.json')
        template = '/config/'.join(template)

        with open(template, 'r') as tmp:
            self.template = json.load(tmp)

    def deploy_message_parser(
        self,
        song_number: str,
        song_name: str,
        song_artist: str
    ) -> str:
        """ format the music deployment message """

        message = '\n'.join(self.template['music']['deploy_message'].format(
            song_number, song_name, song_artist))

        return(message)
