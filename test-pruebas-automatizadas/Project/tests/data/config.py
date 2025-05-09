import os
import json

settings = None

#Load environment test automations
def load_settings(settings_env="environment_t.json"):
    global settings
    try:
        path_settings = os.path.join(os.path.dirname(os.path.abspath(__file__)), settings_env.strip('"'))
        with open(path_settings, 'r') as f:
            settings = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found:'{settings_env}'")
    except json.JSONDecodeError as e:
        raise ValueError(f"Json settings error: {e}")

load_settings()
