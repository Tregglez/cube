from pathlib import Path
import tomllib
from getpass import getpass
import requests


# --- Settings ---
# Cube's settings live outside the project, so the server address
# and username are never uploaded to GitHub.
config_path = Path.home() / ".config/cube/config.toml"

with open(config_path, "rb") as f:
    config = tomllib.load(f)

amp_url = config["amp"]["url"]
username = config["amp"]["username"]

# Asked for each time and never saved, so it only ever lives in memory.
password = getpass("AMP Password: ")

# AMP answers in JSON when asked to. Every request uses these headers.
headers = {"Accept": "application/json"}


# --- Log in ---
# Same login as the web panel. "token" is for two-factor codes (not used).
login_payload = {
    "username": username,
    "password": password,
    "token": "",
    "rememberMe": False,
}

login_response = requests.post(amp_url + "/API/Core/Login", json=login_payload, headers=headers)
login_result = login_response.json()

# Stop here if the login failed, so nothing below runs without a session.
if not login_result["success"]:
    print("Login failed")
    exit()

print("Welcome to Cube")

# The session ID proves we're logged in. Every request from now on sends it.
session_id = login_result["sessionID"]


# --- Servers ---
# Ask AMP's controller (ADS) for every instance it manages.
instances_payload = {"SESSIONID": session_id}

instances_response = requests.post(amp_url + "/API/ADSModule/GetInstances", json=instances_payload, headers=headers)
instances_result = instances_response.json()

# Selecting the list with the location of the games.
instances = instances_result[0]["AvailableInstances"]

appstate_number = {
    20: "Running",
    100: "Offline",
    50: "Sleeping"
}

servers = []

# For logic Listing out the games.
for game in instances:
    if game['Module'] != "ADS":
        # Takes an empty list and adds a game to the list.
        servers.append(game)


for number, game in enumerate(servers, start=1):
    app_state = appstate_number.get(game["AppState"], "Unknown")

    # Number of players is displayed in these variables.
    players_online = game["Metrics"]["Active Users"]["RawValue"]
    player_limit =  game["Metrics"]["Active Users"]["MaxValue"]

    # The display of all the servers.
    print(f"{number}. {game['FriendlyName']}  |  Server Type: {game['Module']}  |  {app_state}  |  {players_online}/{player_limit}")

