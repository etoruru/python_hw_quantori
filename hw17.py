#!/usr/bin/env python3

from exif import Image

with open('1.jpeg', 'rb') as palm_file:
    palm_image = Image(palm_file)

try:
    with open('gps_file.txt', 'w') as f:
	    f.write(f'{palm_image.gps_latitude}; {palm_image.gps_longitude}')
except Exception:    
    print("does not contain any EXIF information.")






