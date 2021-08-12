"""
Vykdom Bot Cuter Functions
~~~~~~~~~~~~~~~~~~~

Functions that are too ugly will be put here for the Vykdom Discord Bot.

:copyright: (c) 2021-present Meaning
:license: GNU General Public License v3.0, see LICENSE for more details.
"""
import discord

from random_word import RandomWords
from Functions import Roblox, DB
from Objects import Errors

## Cogs.Database.py

async def verify_user(ctx, client):
    if not isinstance(ctx.channel, discord.DMChannel):
        await ctx.reply("Verification Process in DM's")
    first_message = await ctx.author.send("What is your Roblox Username (Case Sensitive) or Roblox ID?")

    checkMessage = lambda message : message.channel == first_message.channel and message.author == ctx.author
    checkReaction = lambda reaction, user : reaction.message.channel == first_message.channel and user == ctx.author and reaction.emoji in ['✅', '❌']

    name_message = await client.wait_for('message', check=checkMessage)

    try:
        try:
            roblox_user = Roblox.getUserFromID(int(name_message.content))
        except:
            roblox_user = Roblox.getUserFromName(name_message.content)
    except Errors.RobloxNamesNotFound or Errors.RobloxUserNotFound:
        await ctx.send("Could not find any User.\nTry again and make sure its case sensitive.")
        return

    checking = await ctx.author.send(
        content="Is this you?",
        embed=roblox_user.embed().set_author(name="React with ✅ If it is else ❌")
    )

    await checking.add_reaction("✅")
    await checking.add_reaction("❌")

    reac, usr = await client.wait_for('reaction_add', check=checkReaction)

    if reac.emoji == '❌':
        await ctx.author.send("Try again.")
        return

    async with ctx.author.typing():
        code = " ".join([RandomWords().get_random_word() for _ in range(5)])
        verification_message = await ctx.author.send(f"Set this code to your About: {code}\n\nReact when complete!")
        await verification_message.add_reaction("✅")

    reac, usr = await client.wait_for('reaction_add', check=checkReaction)

    roblox_user2 = Roblox.getUserFromID(roblox_user.id)

    return (roblox_user2, code in roblox_user2.description)