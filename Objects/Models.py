"""
Vykdom Bot Models
~~~~~~~~~~~~~~~~~~~

Models for the Vykdom Discord Bot.

:copyright: (c) 2021-present Meaning
:license: GNU General Public License v3.0, see LICENSE for more details.
"""

import discord
import datetime
from discord.ext import commands


"""
RUser
"""


class RUser:
    
    def __init__(self, roblox_data):
        self.display_name = roblox_data["displayName"]
        self.name = roblox_data["name"]
        self.id = roblox_data["id"]
        self.banned = roblox_data["isBanned"]
        self.created = datetime.datetime.strptime(
            roblox_data["created"],
            "%Y-%m-%dT%H:%M:%S.%fZ"
        )

############################################################################

"""
Vyktranian
    .id
    .name
    .discriminator
        .avatar()
    .convert() # For funtion formatting 
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

#####################################################################################

"""
Award
    .id
    .name
    .accolades
"""


class Medal:
    """Medal

    This represents an Vyktranian award
    """

    def __init__(self):
        pass

    @classmethod
    async def convert(ctx, argument):
        pass