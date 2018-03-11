class Player:

    def __init__(self, character, place):
        self.character = character
        self.place = place

    def get_place(self):
        return self.place

    def get_character(self):
        return self.character

    def fight(self, opponent):
        return opponent.get_character().get_weightage()
