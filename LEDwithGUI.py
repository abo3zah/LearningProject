import RPi.GPIO as GPIO
import time
from guizero import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(26, GPIO.IN)

# confirmation message after closure
def do_this_on_close():
    if yesno("Close", "Do you want to quit?"):
        GPIO.output(4, GPIO.LOW)
        app.destroy()

# setting app the name
def switcher():
    global LEDstatus
    if LEDstatus == False:
        GPIO.output(4, GPIO.HIGH)
        LEDstatus = True
    else:
        GPIO.output(4, GPIO.LOW)
        LEDstatus = False
        
#initialization for LED
LEDstatus = False

#initializing the app
app = App(title="Hello World")

#adding a text and setting the default value
welcome_message = Text(app, text="LED switcher", color="Red")

#adding a pushbutton
update_text= PushButton(app, command=switcher, text="switch LED")

# When user tries to close the app
app.on_close(do_this_on_close)

app.display()