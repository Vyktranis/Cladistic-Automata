"""
Vykdom Bot Errors
~~~~~~~~~~~~~~~~~~~

Errors for the Vykdom Discord Bot.

:copyright: (c) 2021-present Meaning
:license: GNU General Public License v3.0, see LICENSE for more details.
"""

## ROBLOX API CUSTOM EXCEPTIONS

class RobloxUserNotFound(Exception):
    """RobloxUserNotFound

    This Error is used when the roblox api returns none users found.
    """
    pass

class RobloxNamesNotFound(Exception):
    """RobloxNamesNotFound

    This Error is used when the roblox api cannot find certain names.
    """
    pass

