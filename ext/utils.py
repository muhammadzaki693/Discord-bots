import discord
from discord.ext import commands
import random
import json

def developer():
  def wrapper(ctx):
    with open('data/data.json') as f:
      devs = json.load(f)
      dev = devs["owner"]
      if ctx.author.id == dev:
        return True
  return commands.check(wrapper)

def friends():
  def fwrapper(ctx):
    with open('data/data.json') as fs:
      friends = json.load(fs)
      friends = friends["special"]
      if ctx.author.id in friends:
        return True
  return commands.check(fwrapper)

def random_color():
    color = ('#%06x' % random.randint(8, 0xFFFFFF))
    color = int(color[1:], 16)
    color = discord.Color(value=color)
    return color