"""
Vykdom Bot Database Functions
~~~~~~~~~~~~~~~~~~~

Database Functions for the Vykdom Discord Bot.

:copyright: (c) 2021-present Meaning
:license: GNU General Public License v3.0, see LICENSE for more details.
"""

import pymongo

from Objects import Errors, Models
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

def add_vyktranian(Vyktranian):
    db["Members"].insert_one(
        Vyktranian.db()
    )

## Find Roblox User

def roblox_user_from_discord_id(discord_id):
    """
    This function gets a roblox user from the database using a discord_id
    """
    cursor = db["Roblox"].find_one({"_id" : discord_id})
    if cursor is None:
        raise Errors.RobloxUserNotInDatabase(f"{discord_id} could not be found in the database")
    else:
        return Models.RUser(cursor)

## Find Vyktranian

def vyktranian_from_discord_id(discord_id):
    """
    This function gets a vyktranian user from a discord ID
    """
    pass