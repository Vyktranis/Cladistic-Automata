"""
Vykdom Bot Database Functions
~~~~~~~~~~~~~~~~~~~

Database Functions for the Vykdom Discord Bot.

:copyright: (c) 2021-present Meaning
:license: GNU General Public License v3.0, see LICENSE for more details.
"""

import pymongo

from config import DB_ADDRESS

db = pymongo.MongoClient(DB_ADDRESS)["VYKTRANIS"]

###### VERIFICATION #######

def verify_account(discord_id, robloxUser):
    """
    This functions add/updates the roblox user in the database

    Commands Linked:
        - Verify
        - Reverify
        - Update
    """
    try:
        db["Roblox"].insert_one({
            "_id" : discord_id,
            "displayName" : robloxUser.display_name,
            "name" : robloxUser.name,
            "id" : robloxUser.id,
            "isBanned" : robloxUser.banned,
            "description" : robloxUser.description,
            "profile" : robloxUser.profile
        })
    except:
        db["Roblox"].update_one(
            {"_id" : discord_id},
            {
                "$set" : {
                    "displayName" : robloxUser.display_name,
                    "name" : robloxUser.name,
                    "id" : robloxUser.id,
                    "isBanned" : robloxUser.banned,
                    "description" : robloxUser.description,
                    "profile" : robloxUser.profile
                }
            }
        )
