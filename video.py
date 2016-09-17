from __future__ import print_function
from dronekit import connect, VehicleMode
import cv2
import sys
import time



# Connect to UDP endpoint (and wait for default attributes to accumulate)
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
#print 'Connecting to ' + target + '...'
vehicle = connect(target, wait_ready=True)



def rgb_encode(red, green, blue):
    return 16 + (int(red*6) * 36) + (int(green*6) * 6) + int(blue*6)

def print_color(*args, **kwargs):
    fg = kwargs.pop('fg', None)
    bg = kwargs.pop('bg', None)

    set_color = ''
    if fg:
        set_color += '\x1b[38;5;%dm' % rgb_encode(*fg)
    if bg:
        set_color += '\x1b[48;5;%dm' % rgb_encode(*bg)
    print(set_color, end='')
    print(*args, **kwargs)
    print('\x1b[0m', end='')

# Open /dev/video0
vc = cv2.VideoCapture()
vc.open(0)

# Start our printing loop.
interval = .5
last = time.time()
while True:
    # Grab a frame. Then retrieve it from the buffer.
    vc.grab()
    ret, buf = vc.retrieve()
    #cv2.imwrite("/Users/Simeon/Documents/img.jpeg")
    if not ret:
        SystemExit('Could not retrieve image.')

    # Get a tuple of (r, g, b) as float values.
    rgb = [x/255.0 for x in cv2.mean(buf)[2::-1]]

    # Wait for our interval to have elapsed.
    next = time.time()
    if next - last < interval:
        time.sleep(interval - (next - last))
    last = time.time()

    # Print out hex color and a color strip.
    print('Average hex color: 0x%02X%02X%02X    ' % tuple([int(x*255) for x in rgb]), end='')
    print_color('          ', bg=rgb, end='')
    print(' ')
