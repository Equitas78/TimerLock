# TimeLock
This is a work in progress project for controlling kids time on computers

Cloud Server would solve a lot of the administration and granular configuration
For now, the compiling would require that the TimeLock exe is part of the Run in the registry in Regedit for windows
Also the code is only relevant for one screen. Multiple screens are not yet blocked.

# Add Admin form to adjust time
# If computer is restarted, Timer should continue from where it started
	- if the time is finished and windows is restarted, lock screen should be immediate
	- if time not finished, than timer should continue counting down from where it stopped.
# Make the program resilient to being shutdown from Task Manager
# Add functionality to extend time
# Add automated tasks when time is up and password is or isn't typed: auto-shutdown, extend time etc...
# Fix multi-screen lock
# Build iOS App to control computers
	- connection to cloud to store remaining time
	- will open multiple capabilities to add calendars and more tailored time restriction
	

**Installation**
Install python (i did the dev in VSCode free from microsoft)
  - install tk library: pip install tk
  - time library is installed by default with python
  - pyinstaller will allow you to compile the file as a windows executable: pip install pyinstaller
    you can then use the following command to compile: pyinstaller --onefile --noconsole TimerLock.py (it will create TimeLock.exe file as one file and will remove the terminal console from showing)
