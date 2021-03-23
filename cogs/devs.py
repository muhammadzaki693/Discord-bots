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
    
    @commands.command()
    @utils.developer()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down....")
        await bot.logout()