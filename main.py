import os
import discord
from discord.ext import commands
from numpy import random

client = commands.Bot(command_prefix="!")
token = os.environ['token']
ideas = ['Decorate the server', 'Add a welcome bot', 'Add an admin bot', 'Run a competition', 'Add new emotes', 'Invite new people to the server', 'Hope on voice chat', 'Share a project you\'re working on', ]


@client.event
async def on_ready():
    print("ready")


@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am your bot!")


@client.command()
async def idea(ctx):
  rand = random.randint(7)
  await ctx.send(ideas[rand])


client.run(token)
