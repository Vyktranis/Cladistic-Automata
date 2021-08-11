import discord
from discord.ext import commands

class Audit(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener
    async def on_message_delete(self, message):
        pass

    @commands.Cog.listener
    async def on_message_edit(self, before, after):
        pass

    @commands.Cog.listener
    async def on_member_update(self, before, after):
        pass

    @commands.Cog.listener
    async def on_member_join(member):
        pass

    @commands.Cog.listener
    async def on_member_remove(member):
        pass

    @commands.Cog.listener
    async def on_user_update(self, before, after):
        pass

def setup(client):
    client.add_cog(Audit(client))