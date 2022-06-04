from dispatcher import _dispatcher, bot
from core.commands import setup_commands
from core.events import setup_events


if __name__ == '__main__':
    setup_commands()
    setup_events()

    bot.run(_dispatcher().return_token())