##############################
#    VYKTRANIS MAIN BOT      #
##############################

# IMPORTS

import discord
from discord.colour import Color
from discord.ext import commands

import Objects
from Functions import *
from config import BOT_TOKEN

################################

# Bot Creation
client = commands.Bot(
    command_prefix=commands.when_mentioned_or("c!"), 
    intents=discord.Intents.all(),
    description="Cladistic Automata made for the Vyktranis Discord Servers",
    case_insensitive=True
)

def embedFormat(user):
    e = discord.Embed(
        title="『 ۩ 』»› __**CLADISTIC PROFILE**__",
        description="""```diff
-  ᚛ ▬▬▬▬▬▬▬▬▬▬▬▬▬〘PROGRESS〙▬▬▬▬▬▬▬▬▬▬▬▬▬ ᚜  -```
🟥 🟥 🟥 🟥 🟥 🟥 🟥 🟥 🟥 ⬛ • **99%**""",
        colour=0xb10f0f,
        url=user.link()
    )
    e.set_thumbnail(url=user.profile)
    return e

@client.event
async def on_ready():
    print("Online")

@client.command()
async def test(ctx, id : int):
    rUser = Roblox.getUserFromID(id)
    await ctx.send(embed=embedFormat(rUser))

client.load_extension("Cogs.Database")

client.run(BOT_TOKEN)