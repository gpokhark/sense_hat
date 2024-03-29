from sense_hat import SenseHat
import time
def GpClock(sense: SenseHat):
    # sense = SenseHat()
    
    # sense.set_rotation(270)
    sense.low_light = True
    
    number = [
        0,1,1,1,  # Zero
        0,1,0,1,
        0,1,0,1,
        0,1,1,1,
        0,0,1,0,  # One
        0,1,1,0,
        0,0,1,0,
        0,1,1,1,
        0,1,1,1,  # Two
        0,0,1,1,
        0,1,1,0,
        0,1,1,1,
        0,1,1,1,  # Three
        0,0,1,1,
        0,0,1,1,
        0,1,1,1,
        0,1,0,1,  # Four
        0,1,1,1,
        0,0,0,1,
        0,0,0,1,
        0,1,1,1,  # Five
        0,1,1,0,
        0,0,1,1,
        0,1,1,1,
        0,1,0,0,  # Six
        0,1,1,1,
        0,1,0,1,
        0,1,1,1,
        0,1,1,1,  # Seven
        0,0,0,1,
        0,0,1,0,
        0,1,0,0,
        0,1,1,1,  # Eight
        0,1,1,1,
        0,1,1,1,
        0,1,1,1,
        0,1,1,1,  # Nine
        0,1,0,1,
        0,1,1,1,
        0,0,0,1
    ]
    
    hour_color = [0,0,255]  # Blue
    minute_color = [255,2,0]  # Green
    empty = [0,0,0]  # Black
    
    clock_image = [
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0
    ]
    
    # Display clock for 10 seconds
    count = 0

    while count < 10:
        count += 1
        hour = time.localtime().tm_hour
        minute = time.localtime().tm_min

        # Map digits to the clock_image array
        pixel_offset = 0
        index = 0
        for index_loop in range(0, 4):
            for counter_loop in range(0, 4):
                clock_image[index] = number[int(hour/10)*16+pixel_offset]
                clock_image[index+4] = number[int(hour%10)*16+pixel_offset]
                clock_image[index+32] = number[int(minute/10)*16+pixel_offset]
                clock_image[index+36] = number[int(minute%10)*16+pixel_offset]
                pixel_offset = pixel_offset + 1
                index = index + 1
            index = index + 4

        # Color the hours and minutes
        for index in range(0, 64):
            if (clock_image[index]):
                if index < 32:
                    clock_image[index] = hour_color
                else:
                    clock_image[index] = minute_color
            else:
                clock_image[index] = empty

        # Display the time
        sense.low_light = True  # Optional
        sense.set_pixels(clock_image)
        time.sleep(1)