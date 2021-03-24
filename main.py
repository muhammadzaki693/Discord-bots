import discord
import asyncio
import os
import json
import random
from discord.ext import commands
#from cogs import development, devs, member
from ext import utils
from keep_alive import keep_alive
from pretty_help import PrettyHelp, Navigation

cogss = [
  "cogs.member",
  "cogs.devs",
  "cogs.development"
]

async def animationstatus():
    await bot.wait_until_ready()
    
    statuses = ["code", f"{len(bot.guilds)} server | > help", "discord.py", "python"]
    
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(10)

bot = commands.Bot(command_prefix=commands.when_mentioned_or('>',':','$','<','_','%'),help_command=None)

@bot.event
async def on_ready():
    print("bot online")

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
	  msg = await ctx.send("[>")
	  await asyncio.sleep(1)
	  await msg.edit(content="[>>")
	  await asyncio.sleep(1)
	  await msg.edit(content="[>>>")
	  await asyncio.sleep(1)
	  await msg.edit(content="[>>>>")
	  await asyncio.sleep(1)
	  await msg.edit(content="[>>>>>")
	  await asyncio.sleep(1)
	  await msg.edit(content="[>>>>>>")
	  await asyncio.sleep(1)
	  await msg.edit(content="[>>>>>>>")
	  await asyncio.sleep(1)
	  await msg.edit(content="[>>>>>>>>")
	  await asyncio.sleep(1)
	  await msg.edit(content="[>>>>>>>>>")
	  await asyncio.sleep(1)
	  await msg.edit(content="[>>>>>>>>>>")

keep_alive()
for file in cogss:
  bot.load_extension(file)
bot.loop.create_task(animationstatus())
bot.run(os.getenv("TOKEN"))