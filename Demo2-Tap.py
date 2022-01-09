import time
from adafruit_circuitplayground import cp

cp.detect_taps = 1

while True:
   if cp.tapped:
	cp.play_tone(440, .25)
	cp.pixels.fill((255,255,255))
	cp.pixels.show()
	time.sleep(.5)
	cp.pixels.fill((0,0,0))
	cp.pixels.show()
   time.sleep(.5)


