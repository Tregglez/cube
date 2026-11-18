from pathlib import Path
import tomllib
from getpass import getpass
import requests

# Config location with server details and IP.
config_path = Path.home() / ".config/cube/config.toml"

with open(config_path, "rb") as f:
    config = tomllib.load(f)


# Global Variables
username = config["amp"]["username"]
url = config["amp"]["url"]
password = getpass("AMP Password: ")

# Dictionaries
login_data = {
    "username": username,
    "password": password,
    "token": "",
    "rememberMe": False
}

header = {"Accept": "application/json"}

response = requests.post(url + "/API/Core/Login", json=login_data, headers=header)
data = response.json()

if data["success"]:
    print("Welcome to Cube")
else:
    print("Incorrect Password")