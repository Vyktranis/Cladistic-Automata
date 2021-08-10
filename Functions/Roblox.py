import requests
from ..Objects import Errors

BASE_USER_URL = "https://users.roblox.com/v1/users/{}"

def getRobloxDesc(robloxID):
    data = requests.get(BASE_USER_URL.format(robloxID)).json()
    if "errors" in data:
        raise Errors.RobloxUserNotFound("Could not find this User.")
    return data["description"]
