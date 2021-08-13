"""
Vykdom Bot Database Functions
~~~~~~~~~~~~~~~~~~~

Database Functions for the Vykdom Discord Bot.

:copyright: (c) 2021-present Meaning
:license: GNU General Public License v3.0, see LICENSE for more details.
"""

import discord
import pymongo

from Objects import Errors, Models
from config import DB_ADDRESS

db = pymongo.MongoClient(DB_ADDRESS)["VYKTRANIS"]

###### VERIFICATION #######

def verify_account(discord_user, robloxUser):
    """
    This functions add/updates the roblox user in the database

    Commands Linked:
        - Verify
        - Reverify
        - Update
    """
    try:
        db["Members"].insert_one({
            "_id" : discord_user.id,
            "name" : discord_user.name,
            "discriminator" : discord_user.discriminator,
            "timezone" : "Eastern Standard Time",
            "rank" : {
                "id" : 0,
                "name" : "Verified",
                "description" : "Verified through the Bot",
                "accolades" : 0,
                "family" : ""
            },
            "medals" : [],
            "accolades" : 0
        })
    except pymongo.errors.DuplicateKeyError:
        pass
    finally:
        try:
            db["Roblox"].insert_one({
                "_id" : discord_user.id,
                "displayName" : robloxUser.display_name,
                "name" : robloxUser.name,
                "id" : robloxUser.id,
                "isBanned" : robloxUser.banned,
                "description" : robloxUser.description,
                "profile" : robloxUser.profile,
                "created" : robloxUser.created
            })
        except:
            db["Roblox"].update_one(
                {"_id" : discord_user.id},
                {
                    "$set" : {
                        "displayName" : robloxUser.display_name,
                        "name" : robloxUser.name,
                        "id" : robloxUser.id,
                        "isBanned" : robloxUser.banned,
                        "description" : robloxUser.description,
                        "profile" : robloxUser.profile,
                        "created" : robloxUser.created
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
        return cursor

## Find Vyktranian

def vyktranian_from_discord_id(discord_id):
    """
    This function gets a vyktranian user from a discord ID
    """
    cursor = db["Members"].find_one({"_id" : discord_id})
    if cursor is None:
        raise Errors.VyktranisUserNotInDatabase(f"{discord_id} could not be found in the database")
    else:
        return cursor

# Get Rank

def rank_by_id(rank_id):
    """
    This function gets a rank from the id
    """
    cursor = db['Ranks'].find_one({"_id" : rank_id})
    return cursor