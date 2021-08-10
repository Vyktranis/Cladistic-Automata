##############################
#    VYKTRANIS MAIN BOT      #
##############################

# IMPORTS

import discord
from discord.ext import commands

import Objects
from .config import BOT_TOKEN

################################

# Bot Creation
client = commands.Bot(
    command_prefix=commands.when_mentioned_or("a!"), 
    intents=discord.Intents.all(),
    description="Cladistic Automata made for the Vyktranis Discord Servers",
    case_insensitive=True
)

@client.event
async def on_ready():
    print("Online")

client.run(BOT_TOKEN)