import discord
import requests
import secrets
import datetime

from discord.ext import commands
from Functions import Roblox, DB, Cuter
from Objects import Errors, Models

class Database(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name="Verify")
    async def _verify(self, ctx):
        """Verifies a User's Roblox account through the bot."""

        user, verified, tz = await Cuter.verify_user(ctx, self.client)

        if verified:
            DB.verify_account(ctx.author, user, tz)
            await ctx.author.send("Account Linked")
        else:
            await ctx.author.send("Failed, Please try again.")

    @commands.command()
    async def profile(self, ctx, user : Models.Vyktranian = None):
        """Shows you or someone else's profile"""
        user = user if user is not None else await Models.Vyktranian.convert(ctx, str(ctx.author.id))
        await user.display(ctx)

    @commands.command()
    async def update(self, ctx, time):
        """Test Command for the time being"""
        pass

    @commands.command()
    async def setchannel(self, ctx, channelType):
        """Set's a channel to a specific type"""
        if channelType.lower() == "verify":
            pass
        elif channelType.lower() == "commands":
            pass
        else:
            await ctx.send("That is not a valid Channel Type.")

def setup(client):
    client.add_cog(Database(client))