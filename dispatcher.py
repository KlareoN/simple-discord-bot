from discord import Intents
from discord.ext import commands


class _dispatcher:
    def __init__(self):
        self.__token = ''

    def return_token(self):
        return self.__token


bot = commands.Bot(
    command_prefix = '!',
    intents = Intents.all()
)
