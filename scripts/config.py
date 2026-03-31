import json
import os
from pathlib import Path

# Create home/user/.tip-cloud file
CONFIG_DIR = Path.home() / ".tip-cloud"
CONFIG_FILE = CONFIG_DIR / "config.json"

# Cheks if config file exists, if not creates one
def config_check():
    CONFIG_DIR.mkdir(parents = True, exist_ok = True)
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, "w") as file:
            json.dump({}, file)

# Getting config
def get_config():
    config_check()
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

# Updating cofiguration 
def update_config(update_config):
    config_data = get_config()
    config_data.update(update_config)
    with open(CONFIG_FILE, "w") as file:
            json.dump(config_data, file, indent = 4)
    print(f"Updated {list(update_config.keys())}")



