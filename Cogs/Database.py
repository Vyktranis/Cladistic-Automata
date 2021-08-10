import discord

from discord.ext import commands

class Database(commands.cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["reverify"])
    async def verify(self, ctx):

        ## Begin Verification Process
        pass

    @commands.command()
    async def update(self, ctx):
        pass

def setup(client):
    client.add_cog(Database(client))