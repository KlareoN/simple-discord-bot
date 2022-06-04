from dispatcher import bot
from .main import command_main


def setup_commands():
    bot.add_cog(command_main())