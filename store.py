import pickle
import errno

state = None
characters = {
    "luke": {
        "name": "Luke Skywalker",
        "weightage": 100
    },
    "darth": {
        "name": "Darth Vader",
        "weightage": 90
    },
    "leia": {
        "name": "Princess Leia",
        "weightage": 100
    },
    "chewbacca": {
        "name": "Chewbacca",
        "weightage": 50
    },
    "hans": {
        "name": "Hans Solo",
        "weightage": 80
    },
    "jabba": {
        "name": "Jabba The Hutt",
        "weightage": 70
    }
}

places = {
    "tatooine": {
        "name": "Tatooine",
        "characters": ['luke', 'darth', 'jabba']
    },
    "kashyyyk": {
        "name": "Kashyyyk",
        "characters": ['chewbacca']
    },
    "dagobah": {
        "name": "Dagobah",
        "characters": ['yoda', 'luke', 'darth']
    },
    "naboo": {
        "name": "Naboo",
        "characters": ["hans", "leia", "darth"]
    },
    "coruscant": {
        "name": "Coruscant",
        "characters": ['luke', 'darth', 'hans', 'leia']
    }
}


def init_state():
    global state
    state = {'character': None,
             'place': None,
             'experience': 0
             }


def list_characters():
    print "*** Available Characters ***"
    print "Nick Name | Name | Weightage"
    print "-----------------------------"
    for key, value in characters.iteritems():
        print key + " | " + value["name"] + " | " + value.weightage


def list_places():
    print "*** Available Characters ***"
    print "Nick Name | Name | Resident Characters"
    print "--------------------------------------"
    for key, value in places.iteritems():
        print key + " | " + value["name"] + " | " + ', '.join(value["characters"])


def load_game_state():
    global state
    try:
        with open('state.txt', 'rb') as handle:
            state = pickle.loads(handle.read())
    except IOError as e:
        if e.errno == errno.ENOENT:
            init_state()


def write_game_state():
    with open('state.txt', 'wb') as handle:
        pickle.dump(state, handle)


def character_exists(nick_name):
    return True if nick_name in characters else False


def place_exists(nick_name):
    return True if nick_name in places else False


def save_character(nick_name):
    load_game_state()
    state["character"] = nick_name
    write_game_state()


def save_place(place_name):
    load_game_state()
    state["place"] = place_name
    write_game_state()


def save_experience(experience):
    load_game_state()
    state["experience"] = experience + state["experience"]
    write_game_state()


def get_experience():
    return state["experience"]


def get_character_name(nick_name):
    return characters[nick_name]["name"]


def get_weightage(nick_name):
    return characters[nick_name]["weightage"]


def get_place_name(nick_name):
    return places[nick_name]["name"]


def get_characters(nick_name):
    return places[nick_name]["characters"]


def character_exists_at_place(place, character):
    return character in places[place]["characters"]


def get_state():
    load_game_state()
    return state


def reset_state():
    init_state()
    write_game_state()
