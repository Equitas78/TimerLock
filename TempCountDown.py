import time
from ScreenLock import show_lock_screen
from Countdown import create_transparent_box

# Function to start the timer
def start_timer():
    while True:
        elapsed_time = 0
        while elapsed_time < 15:  # Timer runs for 60 minutes
            time.sleep(1)  # Sleep for 1 second
            elapsed_time += 1  # Increment elapsed time by 1 second
            print("elapse time : ", elapsed_time)
            # Check if 45 minutes have passed
            if elapsed_time == 45:
                show_lock_screen(temporary_lock=True, lock_time=15)
                elapsed_time = 0
                time.sleep(15)

create_transparent_box(temporary_lock=False, lock_time=15)
