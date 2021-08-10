##############################
#    VYKTRANIS MAIN BOT      #
##############################

# IMPORTS

import discord

import Objects

from discord.ext import commands

################################

# Bot Creation
vykBot = commands.Bot(
    command_prefix=commands.when_mentioned_or("a!"), 
    intents=discord.Intents.all(),
    description="Cladistic Automata made for the Vyktranis Discord Servers",
    case_insensitive=True
    )

vykbot.run()