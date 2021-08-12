import discord
import asyncio
from discord.ext import commands, tasks
from config import AUDIT_CHANNEL

# FOR TIME BEING IMAGINE AUDIT_CHANNEL HAS A VALUE

class Audit(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.channel = None
        self.get_channel.start()


    @tasks.loop(count = 1)
    async def get_channel(self):
        self.channel = await self.client.fetch_channel(AUDIT_CHANNEL)
        self.get_channel.stop()

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        await self.channel.send(
            embed=discord.Embed(
                title=f"Message Deleted in {message.channel.name}",
                description=message.content
            ).set_author(
                name=str(message.author),
                icon_url=message.author.avatar_url
            ).set_footer(
                text=f"ID: {message.author.id}"
            )
        )

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        # Ignore if a message is larger than a certain length since it will cause errors
        # Will Find a way around it
        if len(before.content) > 1900:
            return
        await self.channel.send(
            embed=discord.Embed(
                title=f"Message Edited in {before.channel.name}"
            ).set_author(
                name=str(before.author),
                icon_url=before.author.avatar_url
            ).add_field(
                name="Before",
                value=before.content
            ).add_field(
                name="After",
                value=after.content
            ).set_footer(
                text=f"ID: {before.author.id}"
            )
        )

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        pass

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        pass

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        pass

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        pass

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        pass

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        pass

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        pass

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        pass

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        pass

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        pass

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        pass

    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        pass

def setup(client):
    client.add_cog(Audit(client))

