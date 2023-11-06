import pickle
import random


def load_state():
    random.seed(1234567890)
    with open("state.dump", "rb") as state_file:
        random.setstate(pickle.load(state_file))


def dump_state():
    with open("state.dump", "wb") as state_file:
        pickle.dump(random.getstate(), state_file)
