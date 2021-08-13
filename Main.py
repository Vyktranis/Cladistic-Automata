##############################
#    VYKTRANIS MAIN BOT      #
##############################

# IMPORTS

import discord
import logging
import random
from discord.ext import commands

from Functions import *
from config import BOT_TOKEN

################################

# Logger

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Bot Creation
client = commands.Bot(
    command_prefix=commands.when_mentioned_or("c!"), 
    intents=discord.Intents.all(),
    description="Cladistic Automata made for the Vyktranis Discord Servers",
    case_insensitive=True
)

def embedFormat(user):
    num = random.randint(0, 100)
    print(num)
    e = discord.Embed(
        title="『 ۩ 』»› __**CLADISTIC PROFILE**__",
        description="""```diff
-  ᚛ ▬▬▬▬▬▬▬▬▬▬▬▬▬〘PROGRESS〙▬▬▬▬▬▬▬▬▬▬▬▬▬ ᚜  -```
{} • **{}%**""".format(
        " ".join(["🟥" for _ in range((100 - num) % 10)]+["⬛" for _ in range(num % 10)]),
        num
    ),
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
client.load_extension("Cogs.Audit")

client.run(BOT_TOKEN)