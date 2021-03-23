import discord
from discord.ext import commands

class development_command(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
    
    @commands.command()
    async def google(self, ctx):
        await ctx.send("development command not a member_command or active commands")