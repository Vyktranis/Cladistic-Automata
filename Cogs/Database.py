from typing_extensions import ParamSpecKwargs
import discord
import requests
import secrets

from discord.ext import commands
from Functions import Roblox, DB, Cuter
from Objects import Errors

class Database(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=["reverify"])
    async def verify(self, ctx):

        user, verified = await Cuter.verify_user(ctx, self.client)

        if verified:
            DB.verify_account(ctx.author.id, user)
            await ctx.author.send("Account Linked")
        else:
            await ctx.author.send("Failed, Please try again.")


    @commands.command()
    async def update(self, ctx):
        pass

    @commands.command()
    async def setchannel(self, ctx, channelType):
        if channelType.lower() == "verify":
            pass
        elif channelType.lower() == "commands":
            pass
        else:
            await ctx.send("That is not a valid Channel Type.")

def setup(client):
    client.add_cog(Database(client))