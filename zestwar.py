import fire

from store import list_characters as listc
from store import list_places as listp
from store import save_character
from store import character_exists
from store import place_exists
from store import save_place
from store import get_state
from store import get_character_name
from store import get_place_name
from store import reset_state
from store import get_characters
from store import get_weightage
from store import character_exists_at_place
from store import save_experience
from store import get_experience as get_total_experience

from models.Character import Character
from models.Place import Place
from models.Player import Player


class Zestwar(object):
    """Zestwar CLI.
    """

    def list_characters(self):
        """
        Lists all the characters that a player can assume
        """
        listc()

    def play_character(self, nick_name):
        """
        Allow a player to assume a character

        Args:
            character_nick_name (str): Nick name of the character
        """
        if character_exists(nick_name):
            save_character(nick_name)
            print "You are now playing character {0}".format(get_character_name(nick_name))
        else:
            print "Character does not exist."

    def list_places(self):
        """
        Lists all the places that a player can explore in the game
        """
        listp()

    def explore_place(self, place_nick_name):
        """
        Allows a player to explore a place

        Args:
            place_nick_name (str): Nick name of the place
        """
        if place_exists(place_nick_name):
            save_place(place_nick_name)
            print "You are now exploring {0}".format(get_place_name(place_nick_name))
            print "The place is known to have {0}".format(', '.join(get_characters(place_nick_name)))
        else:
            print "Place does not exist"

    def fight(self, opponent_nick_name):
        state = get_state()
        character = state['character']

        if not character:
            print "You have not assumed a character yet!"
            print "Run - "
            print "python zestwar.py -- --help"
            return

        character_name = get_character_name(character)
        place = state['place']

        if not place:
            print "You have to explore a place to start fighting!"
            print "Run - "
            print "python zestwar.py -- --help"
            return

        place_name = get_place_name(place)

        if opponent_nick_name == character:
            print "You cannot fight against yourself!"
            return

        if not character_exists_at_place(place, opponent_nick_name):
            print "The character '{0}' does not exist at '{1}' to fight".format(opponent_nick_name, place_name)
            print "Explore {0} again!".format(place)
            return

        # instantiate place
        place = Place(place, place_name, get_characters)
        # instantiate character
        character = Character(character, character_name, get_weightage(character))
        player = Player(character, place)

        opponent_name = get_character_name(opponent_nick_name)
        opponent_character = Character(opponent_nick_name, opponent_name, get_weightage(opponent_nick_name))

        opponent = Player(opponent_character, place)
        experience = player.fight(opponent)
        save_experience(experience)
        print "Congrats! You gained {0} experience points.".format(experience)
        print "Your total experience is now at {0} points".format(get_total_experience())

    def reset(self):
        """
        Reset game - forget everythings
        """
        reset_state()

if __name__ == '__main__':
    fire.Fire(Zestwar)
