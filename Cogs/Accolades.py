from re import L
import discord
from discord.ext import commands

from Objects.Models import Vyktranian

class Accolades(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(case_insensitive=True, invoke_without_command=True)
    async def accolades(self, ctx, users : commands.Greedy[Vyktranian], specification=None, amount : int=None):
        await ctx.reply(f"Users: {users}\nSpecification: {specification}\nAmount: {amount}")

    @accolades.command()
    async def batch(self, ctx, specification, users: commands.Greedy[Vyktranian]):
        pass

def setup(client):
    client.add_cog(Accolades(client))