import typing
import asyncio
import discord
from discord.ext import commands

class Vyktranian:
    """Vykdom Member

    This represents a Vykdom Member

    parms:
        data -- Discord Member or Database Data
    """

    def __init__(self, data):
        pass

    @classmethod
    async def convert(ctx, argument):
        member = commands.MemberConverter.convert(ctx, argument)
        ## DB to get member data
        
        #return cls()
        pass
    
    penis
