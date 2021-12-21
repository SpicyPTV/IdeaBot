import os
import discord
from discord.ext import commands
from numpy import random

client = commands.Bot(command_prefix="!")
token = os.environ['token']
ideas = [
    'Decorate the server', 'Add a welcome bot', 'Add an admin bot',
    'Run a competition', 'Add new emotes', 'Invite new people to the server',
    'Hop on voice chat', 'Share a project you\'re working on',
    'Start a new project', 'Set out a roadmap for your current project',
    'Setup a server wide competition'
]

# Makes sure the bot loads


@client.event
async def on_ready():
    print("ready")
    print(len(ideas))  # Debug


# Basic intro to the Bot's commands


@client.command()
async def hello(ctx):
    await ctx.send(
        "Idea Bot is ready and waiting, just type !idea for an idea in one of your text channels!"
    )


# Command that prints the idea


@client.command()
async def idea(ctx):
    rand = random.randint(11)
    await ctx.send(ideas[rand])


# Authorizes and runs the bot

client.run(token)
