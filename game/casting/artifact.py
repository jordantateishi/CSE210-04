from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):

    def set_text(self, text):
        return super().set_text(text)
    def set_font_size(self, font_size):
        return super().set_font_size(font_size)
    def set_color(self, color):
        return super().set_color(color)
    def set_position(self, position):
        return super().set_position(position)
    def set_message(self):
        message = "messages.txt"
        return message
