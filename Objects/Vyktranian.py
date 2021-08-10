import discord
from discord.ext import commands

"""
User Object
    .id
    .name
    .discriminator
        .avatar()
"""

class Vyktranian:
    """Vykdom Member

    This represents a Vykdom Member

    parms:
        data -- Discord Member or Database Data
    """

    def __init__(self, data):
        self.id
        self.name
        self.discriminator
        self._avatar

    def avatar(self):
        return f"https://cdn.discordapp.com/avatars/{self.id}/{self._avatar}.png"

    @classmethod
    async def convert(ctx, argument):
        member = commands.MemberConverter.convert(ctx, argument)
        ## DB to get member data
        
        #return cls()
        pass


