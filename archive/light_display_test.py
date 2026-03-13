import time
import board
import neopixel


pixel_pin = board.D18
num_pixels = 8

ORDER = neopixel.RGBW
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness = 0.1, auto_write=False, pixel_order=ORDER)

pixels[0] = (0,255,0)
pixels[1] = (0,255,0)
pixels[2] = (0,255,0)
pixels[3] = (0,0,255)
pixels[4] = (0,255,0)
pixels[5] = (0,255,0)
pixels[6] = (0,255,0)
pixels[7] = (0,255,0)

pixels.show()
