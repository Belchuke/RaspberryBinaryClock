from sense_hat import SenseHat, ACTION_RELEASED
import time, datetime
import signal
import sys

hat = SenseHat()

# variabels for on and off pixel color
on = (0, 10, 0)
off = (0, 0, 0)

ShowClock = True # Boolean that determine if clock is showing
clockDisplayHorizontal = True # Boolean that determine rotation
clockDisplay24Hours = True # Boolean that determine 24 hours.
hat.clear() # Clear display


# Display messages on display, and temporary stops showing binary clock.
def ShowMessage(message):
    global ShowClock # Targets global variable
    ShowClock = False
    hat.clear()
    print(message) # Prints to log 
    hat.show_message(message) # Show messages on display
    ShowClock = True

# Event for changing time setting
def PushedVertical(event):
    global clockDisplay24Hours # Targets global variable
    if event.action != ACTION_RELEASED: # unhook actions, to make sure method doesnt run twice
        if clockDisplay24Hours:
            ShowMessage("Clock Change to 12 hours clock")
            clockDisplay24Hours = False
        else:
            ShowMessage("Clock Change to 24 hours clock")
            clockDisplay24Hours = True
 
# Event for changing orientation for binary clock
def PushedHorizontal(event):
    global clockDisplayHorizontal
    if event.action != ACTION_RELEASED:
        if clockDisplayHorizontal:
            ShowMessage("Clock will be horizontal")
            clockDisplayHorizontal = False
        else:
            ShowMessage("Clock will be Vertical")
            clockDisplayHorizontal = True

# On joystick push direction events. 
hat.stick.direction_up = PushedVertical
hat.stick.direction_down = PushedVertical
hat.stick.direction_left = PushedHorizontal
hat.stick.direction_right = PushedHorizontal


# Method for displaying clock horizontal
def DisplayHorizontalBinary(value):
    for i in range(len(value)):
        binary_str = '{0:08b}'.format(int(value[i]))
        for x in range(0, 8):
            if binary_str[x] == "1":
                hat.set_pixel(x, i+3, on)
            else:
                hat.set_pixel(x, i+3, off)

# Method for displaying clock vertical
def DisplayVerticalBinary(value):
    for i in range(len(value)):
        binary_str = '{0:04b}'.format(int(value[i]))
        for x in range(len(binary_str)):
            if binary_str[x] == '1':
                hat.set_pixel(i, 4+x, on)
            else:
                hat.set_pixel(i, 4+x, off)

# Main Clock Method 
def DisplayBinaryClock():
    now = datetime.datetime.now() # now is a time object
    if clockDisplay24Hours:
        name = now.strftime('%H:%M:%S') # Time string to 24 hours
    else:
        name = now.strftime('%I:%M:%S') # Time string to 12 hours

    if clockDisplayHorizontal:
        DisplayHorizontalBinary([name[0:2], name[3:5], name[6:8]])
    else:
        DisplayVerticalBinary(name[0:2]+"0"+name[3:5]+"0"+name[6:8])


# Method when the program close down.
def signal_handler(sig, frame):
    ShowMessage("Programmet lukker")
    sys.exit(0)

# Method when the program start up
def main(): 
    ShowMessage("Programmet starter")
    while True:
        if ShowClock:
            DisplayBinaryClock()
        time.sleep(1)

signal.signal(signal.SIGINT, signal_handler)

if __name__=="__main__": 
    main()
