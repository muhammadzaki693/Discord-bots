import discord
from ext import utils
from discord.ext import commands

class owner_command(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
    
    @commands.command(name='eval')
    @utils.developer()
    async def _eval(self, ctx,*,code):
        await ctx.send(eval(code))
    
    @commands.command(hidden=True)
    @utils.developer()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down....")
        await self.bot.logout()
    
    @commands.command(hidden=True)
    @utils.developer()
    async def load(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(hidden=True)
    @utils.developer()
    async def unload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name="reload", hidden=True)
    @utils.developer()
    async def _reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


def setup(bot):
  bot.add_cog(owner_command(bot))