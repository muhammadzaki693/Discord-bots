import discord
import requests
import json
from discord.ext import commands

#function
def get_catfact():
  response2 = requests.get("https://catfact.ninja/fact")
  json_data2 = json.loads(response2.text)
  fact = json_data2["fact"]
  return(fact)

def get_response(msg):
  response3 = requests.get(f"https://api.monkedev.com/fun/chat?msg={msg}")
  json_data3 = json.loads(response3.text)
  chat = json_data3["response"]
  return(chat)

def get_reverse(message):
  response4 = requests.get(f"https://api.monkedev.com/fun/reverse?content={message}")
  json_data4 = json.loads(response4.text)
  result = json_data4["result"]
  return(result)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

class member_command(commands.Cog):
    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.bot.latency * 1000)}ms')
    
    @commands.command()
    async def random(self, ctx, mode, *, text):
        if mode == "int":
          embed = discord.Embed()
          embed.title = "int"
          embed.description = f"{random.randint(int(text[0]),int(text[1]))}"
          embed.set_footer(text="int")
          await ctx.send(embed=embed)
        elif mode == "float":
          embed = discord.Embed()
          embed.title = "float"
          embed.description = f"{random.random()}"
          embed.set_footer(text="float")
          await ctx.send(embed=embed)
    
    @commands.command()
    async def info(self, ctx):
        em=discord.Embed(title="userinfo", description="userinfo")
        em.add_field(name="name", value=ctx.author.name, inline=True)
        em.add_field(name="id", value=ctx.author.id, inline=True)
        em.add_field(name="tag",value=ctx.author,inline=True)
        em.add_field(name="server", value=ctx.guild,inline=True)
        em.add_field(name="server id",value=ctx.guild.id,inline=True)
        em.add_field(name="channel",value=ctx.channel,inline=True)
        em.add_field(name="channel id",value=ctx.channel.id,inline=True)
        em.add_field(name="Library", value=f"discord.py")
        await ctx.send(embed=em)
    
    @commands.command()
    async def say(self, ctx, *,text : str):
        await ctx.send(text)
    
    @commands.command(help="")
    async def inspire(self, ctx):
        quote = get_quote()
        await ctx.send(quote)
    
    @commands.command()
    async def chat(self, ctx, *,put: str):
        chat = get_response(put)
        await ctx.send(chat)
    
    @commands.command()
    async def catfact(self,ctx):
        catfacts = get_catfact()
        await ctx.send(catfacts)
    
    @commands.command()
    async def reverse(self,ctx,*,text : str):
        reverse_text = get_reverse(text)
        await ctx.send(reverse_text)