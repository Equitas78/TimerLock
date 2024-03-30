import tkinter as tk
import time
import sys

def main():
    # Default time in seconds. Will require either a manual change and recompile or I need to create an admin form which will take some time.
    time_limit = 2 * 60 * 60 

    # I have 
    # time_limit should always be in seconds.
    # like that you can for example just use 10 sec and you will see how the program works.
    # the try is to just simplify testing if you run for example the code from VSCode. 
    # I recommend to block comment this code and just change the time_limit variable above.
    try:
        seconds = int(input("Enter the time limit in hours: "))
        time_limit = seconds
    except ValueError:
        print("Numeric value required.")

    # Create transparent box with countdown
    create_transparent_box(time_limit)

    # Not using EPOCH as defined in UNIX, just normal time UTC.
    time.sleep(time_limit)
    
    # Call the lock screen function that will provide a password entry box and all the screen is black
    # I am thinking of adding at a later stage a random puzzle generator. If the kids solve it they can play a bit more.
    show_lock_screen()

# This unlock function will take the password from the show_lock_screen input and will determine if the screen will be unlocked
def unlock(password_entry, root, error_label):
    password = password_entry.get()
    
    # Hardcoded password for now. It will take some time to work on an admin form and protecting the process from being manually closed etc...
    if password == "hello":  
        # root is basically the screen in windows from tkinter and I want to remove it
        root.destroy()  # Destroy the Tkinter window
        sys.exit(0) # Quit the program properly
        
    else:
        # If password is wrong, get a message and clear the password text box
        # I don't think its relevant to add a counter here to protect from brute force
        error_label.config(text="Incorrect password. Please try again.")  
        password_entry.delete(0, tk.END)
         

# Countdown box that shows remaining time
def update_countdown(label, remaining_time):
    label.config(text=f"Time left: {remaining_time//3600} hours {(remaining_time%3600)//60} minutes {remaining_time%60} seconds")

# Build and display the Countdown box that shows remaining time
def create_transparent_box(time_limit):
    # Create transparent window on the bottom right corner
    transparent_window = tk.Tk()
    transparent_window.attributes('-alpha', 0.5)  # Set transparency level (0 is fully transparent, 1 is fully opaque)
    transparent_window.overrideredirect(True)  # Remove window decorations
    transparent_window.geometry("+1500+900")  # Position the window at the bottom right corner
    transparent_window.configure(background='black')  # Set background color to black

    # Countdown label
    countdown_label = tk.Label(transparent_window, text="", fg="white", bg="black", font=("Helvetica", 12))
    countdown_label.pack(side="bottom", padx=10, pady=10)

    # Update countdown every second
    remaining_time = time_limit  # Initial remaining time
    update_countdown(countdown_label, remaining_time)

    # This function will update the timer and when time hits 0, the lock screen will popup with password
    def update():
        nonlocal remaining_time
        if remaining_time > 0:
            remaining_time -= 1
            update_countdown(countdown_label, remaining_time)
            countdown_label.after(1000, update)  # Call update function after 1 second
        else: 
            show_lock_screen()    

    update()

    transparent_window.mainloop()
    
# main function using TKINTER library for windows forms etc...
def show_lock_screen():
    
    # my understanding is that root is the main root of the display in windows. I will create a fully black form covering the full screen
    # I will then add the box for password, unlock button action calling the unlock function
    # each component is easy to identify and self explanatory.
    
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background='black') 

    label = tk.Label(root, text="Enter password to unlock", fg="white", bg="black", font=("Helvetica", 24))
    label.pack(pady=50)

    error_label = tk.Label(root, text="", fg="red", bg="black", font=("Helvetica", 12))  # Error message label
    error_label.pack(pady=10)

    password_entry = tk.Entry(root, show='*')
    password_entry.pack(pady=10)

    unlock_button = tk.Button(root, text="Unlock", command=lambda: unlock(password_entry, root, error_label))
    unlock_button.pack(pady=10)

    root.mainloop()

# As this is a simple file, I don't want it to be used as part of imports.
# my understanding is that it helps force that main() is run directly, this is some kind of python coding good habit.
if __name__ == "__main__":
    main()