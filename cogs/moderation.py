import discord
from discord.ext import commands

class member_command(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
    
    @commands.group(name='channel')
    async def channel(self, ctx):
        await ctx.send("you want to create channel or delete?")
    
    @channel.command(name="create")
    async def create(self,ctx,name):
        await ctx.send("success")

def setup(bot):
  bot.add_cog(moderation_command(bot))