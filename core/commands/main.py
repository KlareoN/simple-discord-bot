from dispatcher import bot, commands


class command_main(commands.Cog):
    def __init__(self):
        self._bot = bot

    @commands.command(name = 'hello')
    async def test(self, ctx):
        await ctx.reply('Hello World')