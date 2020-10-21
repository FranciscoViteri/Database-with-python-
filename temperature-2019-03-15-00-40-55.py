# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/temperature-2019-03-15-00-40-55.py"

from sense_emu import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp = sense.temp
    pixels = [red if i < temp else blue for i in range(64)]
    sense.set_pixels(pixels)
