from adapt.intent import IntentBuilder
from chatterbox.skills import ChatterboxSkill
from chatterbox import intent_handler
from os import mkdir
from os.path import join
class FlashCardSkill(ChatterboxSkill):
    def initialize(self):
        data_dir = "data"
        if not self.file_system.exists(data_dir):
            mkdir(join(self.file_system.path, data_dir))

    @intent_handler('show.me.flashcards.intent')
    def handle_do_you_like(self, message):
        self.speak("hey, you are in the handle do you like")
        # nbFlashcards = message.data.get('number')
        # if nbFlashcards is not None:
        #     # self.speak_dialog('like.tomato.type', {'type': tomato_type})
        #     self.speak("number of wanted flashcards : " + str(nbFlashcards))
        # else:
        #     self.speak("number of wanted flashcards not specified")
        #     # self.speak_dialog('like.tomato.generic')


def create_skill():
    return FlashCardSkill()