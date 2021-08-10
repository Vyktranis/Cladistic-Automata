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
from Functions import Roblox


"""
RUser
    .display_name
    .name
    .id
    .banned
    .profile
    .created
        .link()
"""


class RUser:
    """Vykdom Member

    This represents a Vykdom Member

    parms:
        Roblox_data -- Discord Member or Database Data
        Member
    """
    
    def __init__(self, roblox_data):
        self.display_name = roblox_data["displayName"]
        self.name = roblox_data["name"]
        self.id = roblox_data["id"]
        self.banned = roblox_data["isBanned"]
        self.profile = Roblox.getUserThumbnailFromID(self.id)
        self.created = datetime.datetime.strptime(
            roblox_data["created"],
            "%Y-%m-%dT%H:%M:%S.%fZ"
        )

    def link(self):
        return f"https://www.roblox.com/users/{self.id}/profile"


############################################################################

"""
Vyktranian
    .id
    .name
    .discriminator
        .avatar()
    .convert() # For function formatting 
"""

class Vyktranian:
    """Vykdom Member

    This represents a Vykdom Member

    parms:
        data -- Discord Member or Database Data
    """

    def __init__(self, data, *, discord=None, roblox=None):
        self.id
        self.name
        self.discriminator
        self._avatar
        self.discord = discord
        self.roblox = roblox

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
        self.id
        self.name
        self.emoji
        
        pass

    @classmethod
    async def convert(ctx, argument):
        pass