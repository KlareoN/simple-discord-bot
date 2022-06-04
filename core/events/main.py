from dispatcher import bot


class events_main:
    @staticmethod
    @bot.event
    async def on_ready():
        return print('Bot start')

    @staticmethod
    @bot.event
    async def on_message(message):
        await bot.process_commands(message)
