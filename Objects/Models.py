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
from Functions import Roblox, DM

"""
RUser
    .display_name
    .name
    .id
    .banned
    .profile
    .description
    .created
        .link()
"""


class RUser:
    """Roblox Member

    This represents a Roblox Member

    parms:
        Roblox_data -- Discord Member or Database Data
        Member
    """
    
    def __init__(self, roblox_data):
        self.display_name = roblox_data["displayName"]
        self.name = roblox_data["name"]
        self.id = roblox_data["id"]
        self.banned = roblox_data["isBanned"]
        self.description = roblox_data["description"]

        # So that it works whether it is from db or from roblox api
        try:
            self.profile = roblox_data["profile"]
        except:
            self.profile = Roblox.getUserThumbnailFromID(self.id)

        # Sometimes %f is not there.
        # Really fucking stupid
        if isinstance(roblox_data["created"], datetime.datetime):
            self.created = roblox_data["created"]
        else:
            try:
                self.created = datetime.datetime.strptime(
                    roblox_data["created"],
                    "%Y-%m-%dT%H:%M:%S.%fZ"
                )
            except:
                self.created = datetime.datetime.strptime(
                    roblox_data["created"],
                    "%Y-%m-%dT%H:%M:%SZ"
                )

    def link(self):
        return f"https://www.roblox.com/users/{self.id}/profile"

    def embed(self):
        e = discord.Embed(
            title=self.name,
            description=self.description,
            url=self.link()
        )
        e.set_thumbnail(
            url=self.profile
        )
        e.set_footer(
            text=f"ID: {self.id} | Created"
        )
        e.timestamp = self.created
        return e

    @classmethod
    async def convert(ctx, argument):
        member = commands.MemberConverter.convert(ctx, argument)
        return DM.roblox_user_from_discord_id(member.id)



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