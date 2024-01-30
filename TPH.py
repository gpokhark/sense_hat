from sense_hat import SenseHat
from clock_function import GpClock

import time
import subprocess

sense = SenseHat()
sense.low_light = True

# Defind custome colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
clear =(0, 0, 0)

def orientation():
    acceleration = sense.get_accelerometer_raw()

    # Get the components of acceleration
    x = acceleration['x']
    y = acceleration['y']

    theta = 0
    if x > 0.5:
        theta = 270
    elif y > 0.5:
        theta = 0
    elif x < -0.5:
        theta = 90
    elif y < -0.5:
        theta = 180

    sense.set_rotation(theta)

def shutdown():
    # Shutdown the Raspberry Pi
    subprocess.call("sudo shutdown -h now", shell=True)

# Flag to control the loop
running = True

# Set up Sense HAT button event handler
def button_handler(event):
    global running
    if event.action == "pressed":
        sense.clear()
        # Set the orientation
        orientation()
        # Middle button was pressed; initiate shutdown
        sense.show_message("Shutting down", text_colour=red)
        sense.clear()
        time.sleep(1)
        running = False
        shutdown()

# Add event handler for the Sense HAT button
sense.stick.direction_any = button_handler

try:
    while running:
        # Read Temperature, Pressure and Humidity
        temperature = sense.get_temperature()
        pressure = sense.get_pressure()
        humidity = sense.get_humidity()

        # Round the values to one decimal place
        temperature = round(temperature, 1)
        pressure = round(pressure, 1)
        humidity = round(humidity, 1)

        # Set the orientation
        orientation()

        # Create a list of message to display in sequence
        messages_1 = [
            (f"{temperature}C", red),
            (f"{pressure}hPa", green),
            (f"{humidity}%", blue)
        ]

        messages_2 = [
            (f"{temperature}C.", red),
            (f"{pressure}hPa.", green),
            (f"{humidity}%.", blue)
        ]

        # Check if uv4l_raspicam service is running
        service_status = subprocess.getoutput("systemctl is-active uv4l_raspicam")

        if service_status == "active":
            # Display . after the digits
            # Display each message with the corresponding color and a 1-second interval
            for message, color in messages_2:
                sense.show_message(message, scroll_speed=0.05, text_colour=color)
                time.sleep(1)
        else:
	    # Display each message with the corresponding color and a 1-second interval
            for message,color in messages_1:
                sense.show_message(message, scroll_speed=0.05, text_colour=color)
                time.sleep(1)

        # Show Clock
        GpClock(sense)

        # Clear the LED matrix
        sense.clear()

        


except KeyboardInterrupt:
    # Handle a keyboard interrupt (Ctrl + C)
    sense.clear()
    print("Program terminated by user.")
