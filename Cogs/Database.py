import discord
import requests

from discord.ext import commands

class Database(commands.cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=["reverify"])
    async def verify(self, ctx):

        await ctx.reply("Verification Process in DM's")

        dmChannel = await ctx.author.send("What is your Roblox Username")

        def check(message):
            return message.channel == dmChannel.channel and message.author == ctx.author

        name = await self.client.wait_for('message', check=check)





    @commands.command()
    async def update(self, ctx):
        pass

def setup(client):
    client.add_cog(Database(client))