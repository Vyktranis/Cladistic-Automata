"""
Vykdom Bot Errors
~~~~~~~~~~~~~~~~~~~

Errors for the Vykdom Discord Bot.

:copyright: (c) 2021-present Meaning
:license: GNU General Public License v3.0, see LICENSE for more details.
"""

import discord

#### ROBLOX

class RobloxUserNotFound(discord.DiscordException):
    """RobloxUserNotFound

    This Error is used when the roblox api returns none users found.
    """
    pass

class RobloxNamesNotFound(discord.DiscordException):
    """RobloxNamesNotFound

    This Error is used when the roblox api cannot find certain names.
    """
    pass

class RobloxNoThumbnailFound(discord.DiscordException):
    """RobloxNoThumbnailFound

    This Error is used when the roblox api cannot find a users Thumbnail.
    """
    pass

## PYMONGO

class RobloxUserNotInDatabase(discord.DiscordException):
    """RobloxUserNotInDatabase

    This Error is used when a roblox user cannot be found in the database.
    """
    pass

class VyktranianUserNotInDatabase(discord.DiscordException):
    """VyktranianUSerNotInDatabase

    This Error is used when a Vyktranis User cannot be found in the database.
    """
    pass

## Models

class CannotSendToUser(Exception):
    pass