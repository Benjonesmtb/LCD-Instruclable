# Imports
import lcddriver
import time
import datetime
import socket

# set Display
display = lcd.driver.lcd()

# Get IP/ Host
testIP = "8.8.8.8"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((testIP, 0))
ipaddr = s.getsockname()[0]
host = socket.gethostname()

# Get text
text = str(input("Input text:")

# Write to display
 try:
    print("Writing to display")
    display.lcd_display_string(text, 1) # Write line of text to first line of display
    display.lcd_display_string(ipaddr, 3)
    display.lcd_display_string(host, 4)
    while True:
        display.lcd_display_string(str(datetime.datetime.now().time()), 2) # Write just the time to the display
        # Program then loops with no delay (Can be added with a time.sleep)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
