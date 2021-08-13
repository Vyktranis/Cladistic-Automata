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
from Functions import Roblox, DB

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
        return DB.roblox_user_from_discord_id(member.id)



############################################################################

"""
Vyktranian
    .id : int
    .name : str
    .discriminator : int
    .medals : list
    .convert() # For function formatting 
"""

class Vyktranian:
    """Vykdom Member

    This represents a Vykdom Member

    parms:
        data -- Discord Member or Database Data
    """

    def __init__(self, data, discord=None, roblox=None):
        self.id = data["_id"]
        self.name = data["name"]
        self.discriminator = data["discriminator"]
        self.medals = [Medal(i) for i in data["medals"]]
        self.accolades = data["accolades"]
        self.discord = discord
        self.roblox = roblox

    @classmethod
    async def convert(self, ctx, argument):
        member = commands.MemberConverter().convert(ctx, argument)

        #cls(data, )

    async def send(self, *args, **kwargs):
        await self.discord.send(args, kwargs)

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

    def __init__(self, data):
        try:
            self.id = data["id"]
        except:
            self.id = data["_id"]
        self.name = data["name"]
        self.emoji = data["emoji"]

    @classmethod
    async def convert(ctx, argument):
        pass

"""
Rank
    .id
    .name
    .description
    .classification
"""

class Rank:
    """Rank

    This represents a Vykdom Rank.
    """
    
    def __init__(self, data):
        self.id = data["id"] or data["_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.family = data["family"]

    async def convert(ctx, argument):
        pass

    def db(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description,
            "family" : self.family
        }




class Classification:
    pass