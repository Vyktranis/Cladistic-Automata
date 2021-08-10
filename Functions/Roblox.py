import requests
from Objects import Errors, Models

BASE_USER_URL = "https://users.roblox.com/v1/users/{}"
BASE_USER_SEARCH_URL = "https://users.roblox.com/v1/users/search?keyword={}&limit=10"
BASE_USER_THUMBNAIL_URL = "https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={}&size=720x720&format=Png"

def getUserFromID(robloxID):
    """
    This Method returns an RUser Object bassed off a Roblox User ID
    """

    data = requests.get(BASE_USER_URL.format(robloxID)).json()
    if "errors" in data:
        raise Errors.RobloxUserNotFound("Could not find this User.")
    return Models.RUser(data)

def getUserFromName(name):
    """
    This Method returns an RUser Object based off an assumed Roblox Username.
    """

    data = requests.get(BASE_USER_SEARCH_URL.format(name)).json()
    if len(data["data"]) == 0:
        raise Errors.RobloxNamesNotFound("No Users could be found")
    return getUserFromID(data["data"][0]["id"])

def getUserThumbnailFromID(id):
    """
    This Method returns a users thumbnail 
    """

    data = requests.get(BASE_USER_THUMBNAIL_URL.format(id)).json()
    if len(data["data"]) == 0:
        raise Errors.RobloxNoThumbnailFound("Could not find thumbnail")
    return data["data"][0]["imageUrl"]
