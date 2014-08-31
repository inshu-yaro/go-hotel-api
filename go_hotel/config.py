import os
import json

DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config')
CONFIG_FILE = os.path.join(DIR, "application.json")
LOCAL_CONFIG_FILE = os.path.join(DIR, "application.local.json")


def get_config():
    with open(CONFIG_FILE, 'r') as f:
        config = json.loads(f.read())
    if os.path.exists(LOCAL_CONFIG_FILE):
        with open(LOCAL_CONFIG_FILE, 'r') as f:
            local_config = json.loads(f.read())
            config.update(local_config)
    return config

config = get_config()
