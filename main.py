import discord
import asyncio
import os
import json
import random
from discord.ext import commands
from ext import utils
from ext import keep_alive
from pretty_help import PrettyHelp, Navigation

with open("data/auth.json") as f:
  auth = json.load(f)

async def animationstatus():
    await bot.wait_until_ready()
    
    statuses = ("code", f"{len(bot.guilds)} server | > help", "discord.py", "python")
    
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(10)

bot = commands.Bot(command_prefix=commands.when_mentioned_or('>',':','$','<','_','%'),help_command=None)

@bot.event
async def on_ready():
    print(f"""
logged as: {bot.user.name}
bot version: {auth['version']}
-----
cogs

member.py
devs.py
development.py
-----
    """)

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
      return "is bot"
    
    if message.author.id == auth.blacklist:
      return "blacklist"
    
    await bot.process_commands(message)

# custom ending note using the command context and help command formatters
ending_note = "The ending not from {ctx.bot.user.name}\nFor command {help.clean_prefix}{help.invoked_with}"

# ":discord:743511195197374563" is a custom discord emoji format. Adjust to match your own custom emoji.
nav = Navigation("◀️", "▶️")
color = utils.random_color()

bot.help_command = PrettyHelp(
  navigation=nav,
  color=color,
  active_time=30,
  ending_note=ending_note,
  index_title="help",
  no_category="no category cmd"
)

@bot.command()
async def edit(ctx):
	  msg = await ctx.send("[")
	  for i in range(1,11):
	    await asyncio.sleep(1)
	    await msg.edit(content="["+">"*i)

@bot.command()
async def version(ctx):
    await ctx.send(auth["version"])

keep_alive.run()
for file in os.listdir("./cogs"):
  if file.endswith(".py"):
    bot.load_extension(f"cogs.{file[:-3]}")
    print("cogs."+str(file[:-3]),"has loaded")
bot.loop.create_task(animationstatus())
bot.run(auth["TOKEN"])