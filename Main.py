##############################
#    VYKTRANIS MAIN BOT      #
##############################

# IMPORTS

import discord
import logging
import random
from discord.ext import commands, menus

from Functions import *
from config import BOT_TOKEN
from Objects.Pages import VyktranianMenu

################################

# Logger

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

# Bot Creation
client = commands.Bot(
    command_prefix=commands.when_mentioned_or("c!"), 
    intents=discord.Intents.all(),
    description="Cladistic Automata made for the Vyktranis Discord Servers",
    case_insensitive=True
)

@client.event
async def on_ready():
    print("Online")

@client.command()
async def test(ctx):
    m = VyktranianMenu()
    await m.start(ctx)

client.load_extension("Cogs.Database")
client.load_extension("Cogs.Audit")

client.run(BOT_TOKEN)