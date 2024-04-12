from AdminScreen import build_window
import json
import os

#Checking that the config file exists, if not create it
def create_default_config(filename='config.json'):
    if not os.path.exists(filename):
        default_config = {
            "password": "hello",
            "timeLock": "15",
            "MaxContinuousTime":"45"
        }
        with open(filename, 'w') as f:
            json.dump(default_config, f, indent=4)
        print(f"Default configuration created in {filename}")
    else:
        print(f"{filename} already exists, skipping creation.")

# Call the function to create the default config
create_default_config()

#start the admin screen
build_window()