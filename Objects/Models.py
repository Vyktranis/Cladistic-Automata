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
from Objects import Errors
from config import VYKDOMWhite, ACCOLADE, NONACCOLADE

__all__ = (
    'RUser',
    'Vyktranian',
    'Medal',
    'Rank',
    'Clade',
    'Subclade'
)

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

        def __repr__(self):
            attrs = [
                ('id', self.id),
                ('name', self.name),
                ('display_name', self.display_name),
                ('banned' , self.banned),
                ('description', self.description),
                ('profile', self.profile),
                ('created', self.created)
            ]
            innards = ' '.join('%s=%r' % t for t in attrs)
            return f"<{self.__class__.__name__} {innards}>"

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
        .embed()
"""

class Vyktranian:
    """Vykdom Member

    This represents a Vykdom Member

    parms:
        data -- Database Data
        discord -- Discord Member
        roblox -- RUser
    """

    def __init__(self, data, discord=None, roblox=None):
        try:
            self.id = data["_id"]
        except:
            self.id = data["id"]
        self.name = data["name"]
        self.discriminator = data["discriminator"]
        self.timezone = data["timezone"]
        self.rank = Rank(data["rank"])
        self.clade = Clade(data["clade"])
        try:
            self.subclade = Subclade(data["subclade"])
        except:
            self.subclade = None
        try:
            self.departments = [Department(d) for d in data["departments"]]
        except:
            self.departments = None
        try:
            self.medals = [Medal(i) for i in data["medals"]]
        except:
            self.medals = None
        self.accolades = data["accolades"]
        self.discord = discord
        self._user = None
        self.roblox = roblox

    def __str__(self):
        return f"{self.name}#{self.discriminator}"

    def __repr__(self):
        attrs = [
            ('id', self.id),
            ('name', self.name),
            ('discriminator', self.discriminator),
            ('rank' , self.rank),
            ('medals', self.medals),
            ('accolades', self.accolades),
            ('discord', self.discord),
            ('roblox', self.roblox)
        ]
        innards = ' '.join('%s=%r' % t for t in attrs)
        return f"<{self.__class__.__name__} {innards}>"

    def __eq__(self, other):
        return isinstance(self, other) and other.id == self.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def _percent_til_next(self, rank):
        if self.rank.id == 0 and self.accolades == 0:
            return 0
        return round(100 * (self.accolades / rank.accolades))

    def _percent_to_accolade(self, percent):
        before = " ".join([ACCOLADE for _ in range(round(percent / 10))])
    
        after = " ".join(NONACCOLADE for _ in range(round((100 - percent) / 10))) if percent < 100 else ""

        text = before + " " + after
        return text
        
    def json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "discriminator" : self.discriminator,
            "rank" : self.rank.json(),
            "clade" : None,
            "subclade" : None,
            "medals" : None,
            "accolades" : self.accolades
        }

    def db(self):
        return {
            "_id" : self.id,
            "name" : self.name,
            "discriminator" : self.discriminator,
            "rank" : self.rank.json(),
            "clade" : None,
            "subclade" : None,
            "medals" : None,
            "accolades" : self.accolades
        }

    def embed(self):

        next_rank = Rank(DB.rank_by_id(self.rank.id + 1))
        percent = self._percent_til_next(next_rank)

        e = discord.Embed(
            title=f"『 ۩ 』» __**{self.roblox.name}**__",
            description="""
            \♦  ᚛ ▬▬▬▬▬▬▬▬▬▬〘 {0} 〙▬▬▬▬▬▬▬▬▬▬ ᚜  \♦

            > {3} • **{4}%**
            > \u200B
            > {8} {1} remaining to reach `{7}`. ({5} {1})
            > {1} • {6}

            \♦  ᚛ ▬▬▬▬▬▬▬▬▬▬〘 {0} 〙▬▬▬▬▬▬▬▬▬▬ ᚜  \♦
            """.format(
                VYKDOMWhite, 
                ACCOLADE, 
                NONACCOLADE,
                self._percent_to_accolade(percent),
                percent,
                next_rank.accolades,
                self.accolades,
                next_rank.name,
                next_rank.accolades - self.accolades
            ),
            url=self.roblox.link(),
            colour=0xe90000
        )
        e.set_author(
            name="The Vyktranian Dominion\nImperial Convocation Outside the Struggle",
            icon_url="https://t5.rbxcdn.com/cd461fc64aeaa4b332087bfddb7b4b29"
        )
        e.set_thumbnail(
            url=self.roblox.profile
        )
        e.add_field(
            name="__**RANK**__",
            value="> `{}`".format(str(self.rank)),
            inline=False
        ).add_field(
            name="__**CLASSIFICATION**__",
            value="> `{}`".format(self.rank.family or "\u200B"),
            inline=False
        )
        e.add_field(
            name="__**TIMEZONE**__",
            value="> `{}`".format(self.timezone),
            inline=False
        )
        e.add_field(
            name="__**CLADE**__",
            value="> `{}`".format(None),
            inline=False
        )
        e.add_field(
            name="__**SUBCLADE**__",
            value="> `{}`".format(None),
            inline=False
        )
        e.add_field(
            name="__**DEPARTMENT(S)**__",
            value="> {}\n\♦  ᚛ ▬▬▬▬▬▬▬▬▬▬〘 {} 〙▬▬▬▬▬▬▬▬▬▬ ᚜  \♦".format("`None`", VYKDOMWhite),# Later " ".join([f"`{dep}`" for dep in self.departments])
            inline=False
        )
        e.set_footer(
            text="Cladistic Automated Systems",
            icon_url="https://t5.rbxcdn.com/cd461fc64aeaa4b332087bfddb7b4b29"
        )
        e.timestamp = datetime.datetime.utcnow()
        return e

    def set(self, *, timezone=None, rank=None, clade=None, subclade=None, accolades=None):
        if timezone:
            self.timezone = timezone
        if rank:
            self.rank = rank
        if clade:
            self.clade = clade
        if subclade:
            self.subsclade = subclade
        if accolades:
            self.accolades = accolades
            
        DB.update_vyktranian_user(
            self.id,
            tz=timezone,
            rank=rank,
            clade=clade,
            subclade=subclade,
            accolades=accolades
        )

    def add(self, *, departments=None, medals=None, accolades=None):
        if departments:
            if type(departments) == list:
                departments = self.departments + departments
            else:
                departments = self.departments + [departments]
            self.departments = departments
        if medals:
            if type(medals) == list:
                medals = self.medals + medals
            else:
                medals = self.medals + [medals]
            self.medals = medals
        if accolades:
            self.accolades += accolades

        DB.update_vyktranian_user(
            self.id,
            departments=self.departments,
            medals=self.medals,
            accolades=self.accolades
        )
            

    def remove(self, *, departments=None, medals=None, accolades=None):
        if departments:
            if type(departments) == list:
                self.departments = filter(lambda x: x not in departments, self.departments)
            else:
                self.departments.remove(departments)
        if medals:
            if type(medals) == list:
                self.medals = filter(lambda x: x not in medals, self.medals)
            else:
                medals = self.medals + [medals]
        if accolades:
            self.accolades -= accolades

        DB.update_vyktranian_user(
            self.id,
            departments=self.departments,
            medals=self.medals,
            accolades=self.accolades
        )

    @classmethod
    async def convert(cls, ctx, argument):

        member = await commands.MemberConverter().convert(ctx, argument)
        data = DB.vyktranian_from_discord_id(member.id)
        roblox = RUser(DB.roblox_user_from_discord_id(member.id))

        return cls(data, member, roblox)

    async def send(self, *args, **kwargs):
        if self.discord:
            await self.discord.send(*args, **kwargs)
        elif self._user: # Doubt I'd ever get here but just for backup            
            await self._user.send(*args, **kwargs)
        else:
            raise Errors.CannotSendToUser(f"Cannot send PM to {self.name}")



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
        self.description = data["description"]
        self.emoji = data["emoji"]

    @classmethod
    async def convert(cls, ctx, argument):
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
        try:
            self.id = data["id"]
        except:
            self.id = data["_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.accolades = data["accolades"]
        self.family = data["family"]

    def __str__(self):
        return self.name

    def __repr__(self):
        attrs = [
            ('id', self.id),
            ('name', self.name),
            ('description', self.description),
            ('accolades', self.accolades),
            ('family', self.family)
        ]
        innards = ' '.join('%s=%r' % t for t in attrs)
        return f"<{self.__class__.__name__} {innards}>"

    @classmethod
    async def convert(cls, ctx, argument):
        """
        This will look at argument for

        -   ID
        -   Name
        -   RoleID
        """
        pass

    def json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "description"  : self.description,
            "family" : self.family
        }

"""
Clade
    .id
    .name
    .description
"""

class Clade:

    def __init__(self, data):
        try:
            self.id = data["_id"]
        except:
            self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]

"""
Subclade
    .id
    .name
    .description
"""

class Subclade:

    def __init__(self, data):
        try:
            self.id = data["_id"]
        except:
            self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]

"""
Department
    .id
    .name
    .description
"""

class Department:

    def __init__(self, data):
        try:
            self.id = data["_id"]
        except:
            self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]