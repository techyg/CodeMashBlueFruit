import time
from adafruit_circuitplayground import cp
cp.pixels.brightness = 0.3

colors = [[255,0,0],  # red
         [255,150,0], #yellow
         [0,255,0],   #green
         [0,255,255], #cyan
         [0,0,255],   #blue
         [180,0,255], # purple
         [255,255,255]] #white

numcolors = 7
x = 1

while True:
    for c in colors:
        for y in range(0, 10, 1):
            cp.pixels[y] = colors[x-1]
            time.sleep(0.05)
        if x < 7:
            x = x+1
        else:
            x = 1

