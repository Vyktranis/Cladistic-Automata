import discord
import requests
import secrets

from discord.ext import commands
from random_word import RandomWords
from Functions import Roblox, DB
from Objects import Errors

class Database(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=["reverify"])
    async def verify(self, ctx):

        await ctx.reply("Verification Process in DM's")
        first_message = await ctx.author.send("What is your Roblox Username? (Case Sensitive)")
        ### FUNCTIONS

        def checkMessage(message):
            return message.channel == first_message.channel and message.author == ctx.author

        def checkReaction(reaction, user):
            return reaction.message.channel == first_message.channel and user == ctx.author and reaction.emoji in ['✅', '❌']

        name_message = await self.client.wait_for('message', check=checkMessage)

        try:
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

        reac, usr = await self.client.wait_for('reaction_add', check=checkReaction)

        if reac.emoji == '❌':
            await ctx.author.send("Try again.")
            return

        async with ctx.author.typing():
            code = " ".join([RandomWords().get_random_word() for _ in range(5)])
            verification_message = await ctx.author.send(f"Set this code to your About: {code}\n\nReact when complete!")
            
        await verification_message.add_reaction("✅")

        reac, usr = await self.client.wait_for('reaction_add', check=checkReaction)

        roblox_user2 = Roblox.getUserFromID(roblox_user.id)

        if code in roblox_user2.description:
            DB.verify_account(ctx.author.id, roblox_user2)
            await ctx.author.send("Account Linked")
        else:
            await ctx.author.send("Failed, Please try again.")


    @commands.command()
    async def update(self, ctx):
        pass

def setup(client):
    client.add_cog(Database(client))