from gpiozero import Button, LED
import os
import datetime
import time
import sys

led = LED(18)
button = Button(22)

# Flash the LED to show the button has been pressed
button.when_pressed = led.on
button.when_released = led.off

if __name__ == "__main__":
    button.wait_for_press()

    os.system('aplay Dong.wav&') # A good doorbell sound, as all doorbells should have
    os.system('python3 dong-photo.py') # Runs a script to take a photo of the caller, email the owner the photo and the live chat link and save the photo to a firebase database, just in case
    time.sleep(0.1)
    print( "Starting call")
    os.system('python3 dong-call.py') # Starts the video call and sends a link to the owners blynk app using a push notification
    print("Call Ending")
    time.sleep(0.1)
    exit() # Makes sure that the script has ended and all processes are terminate so that it can be restarted fresh.

