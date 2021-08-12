import discord
from discord.ext import commands
from config import AUDIT_CHANNEL

# FOR TIME BEING IMAGINE AUDIT_CHANNEL HAS A VALUE

class Audit(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        # self.channel = client.get_channel(AUDIT_CHANNEL) # UNCOMMENT WHEN WORKING

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
    async def on_member_join(self, member):
        pass

    @commands.Cog.listener
    async def on_member_remove(self, member):
        pass

    @commands.Cog.listener
    async def on_member_ban(self, guild, member):
        pass

    @commands.Cog.listener
    async def on_member_unban(self, guild, member):
        pass

    @commands.Cog.listener
    async def on_user_update(self, before, after):
        pass

    @commands.Cog.listener
    async def on_guild_channel_delete(self, channel):
        pass

    @commands.Cog.listener
    async def on_guild_channel_create(self, channel):
        pass

    @commands.Cog.listener
    async def on_guild_channel_update(self, before, after):
        pass

    @commands.Cog.listener
    async def on_guild_role_delete(self, role):
        pass

    @commands.Cog.listener
    async def on_guild_role_create(self, role):
        pass

    @commands.Cog.listener
    async def on_guild_role_update(self, before, after):
        pass

    @commands.Cog.listener
    async def on_invite_create(self, invite):
        pass

    @commands.Cog.listener
    async def on_invite_delete(self, invite):
        pass

def setup(client):
    client.add_cog(Audit(client))