import tkinter as tk
from ScreenLock import show_lock_screen
from TempScreenLock import temp_lock_screen
import json

with open('config.json') as config_file:
    config = json.load(config_file)   
          
# This is the formatting for the transparent label that will show on the bottom right of the screen
def update_countdown(label, remaining_time):
    label.config(text=f"Time left: {remaining_time//3600} hours {(remaining_time%3600)//60} minutes {remaining_time%60} seconds")


# This is the transparent box. You can change how transparent it is from Attributes.
def create_transparent_box(time_limit):
    transparent_window = tk.Tk()
    transparent_window.attributes('-alpha', 0.5)
    transparent_window.overrideredirect(True)
    transparent_window.geometry("+1500+900")
    transparent_window.configure(background='black')

    countdown_label = tk.Label(transparent_window, text="", fg="white", bg="black", font=("Helvetica", 12))
    countdown_label.pack(side="bottom", padx=10, pady=10)

    # This is where I am forcing the screen to be completely on top
    transparent_window.wm_attributes("-topmost", True)

    remaining_time = time_limit
    update_countdown(countdown_label, remaining_time)
    
    # Update countdown until it finishes and then lock screen.
    def update():
        nonlocal remaining_time
        if remaining_time > 0:

            remaining_time -= 1
            update_countdown(countdown_label, remaining_time)
            countdown_label.after(1000, update)

#I added a Modulo so that every 45 min the timer stops.
#I think there is a better way to do it i.e. configuring based on time spent and not time remaining.
            if ((remaining_time/60)%config('MaxContinuousTime')) == 0:
                transparent_window.destroy()
                temp_lock_screen(config['timeLock']*60)
                remaining_time -= 1
                create_transparent_box(remaining_time)
                
        else:
            show_lock_screen()
            
    update()

    transparent_window.mainloop()
