from mycroft import MycroftSkill, intent_file_handler


class CompanionApp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('app.companion.intent')
    def handle_app_companion(self, message):
        self.speak_dialog('app.companion')


def create_skill():
    return CompanionApp()

