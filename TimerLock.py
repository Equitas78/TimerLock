from AdminScreen import build_window
import json
import os

def create_default_config(filename='config.json'):
    if not os.path.exists(filename):
        default_config = {
            "password": "hello",
            "timeLock": "15",
        }
        with open(filename, 'w') as f:
            json.dump(default_config, f, indent=4)
        print(f"Default configuration created in {filename}")
    else:
        print(f"{filename} already exists, skipping creation.")

# Call the function to create the default config
create_default_config()
build_window()

#from ScreenLock import show_lock_screen
#vfrom Countdown import create_transparent_box


#import adminscreen

# This is where you can specify the time. I need to refactor it later to be able to have it configurable in a good GUI
#def main():
# 
#    global time_limit 
#    time_limit = 2 * 60 * 60 
#    try:
#        seconds = int(input("Enter the time limit in hours: "))
#        time_limit = seconds
#    except ValueError:
#        print("Numeric value required.")
    
#    create_transparent_box(time_limit)
    
#    time.sleep(time_limit)
   
#    show_lock_screen()
  
# Starting the program   
#if __name__ == "__main__":
#    main()
