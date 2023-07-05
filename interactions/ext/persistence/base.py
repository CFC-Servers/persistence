"The base of the extension."

from .persistence import Persistence
def setup(bot, cipher_key=None):
    return Persistence(bot, cipher_key)
