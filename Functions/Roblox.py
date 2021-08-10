import requests
from ..Objects import Errors, Models

BASE_USER_URL = "https://users.roblox.com/v1/users/{}"
BASE_USER_SEARCH_URL = "https://users.roblox.com/v1/users/search?keyword={}&limit=10"

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
        raise Errors.RobloxNamesNotFound("No names could be found")
    return getUserFromID(data["data"][0]["id"])
