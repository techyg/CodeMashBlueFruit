"""
Circuit Playground Bluefruit Ornament Proximity
This demo uses advertising to set the color of scanning devices depending on the strongest broadcast
signal received. Circuit Playgrounds can be switched between advertising and scanning using the
slide switch. The buttons change the color when advertising.
"""

import time
from adafruit_circuitplayground.bluefruit import cpb
from adafruit_circuitplayground import cp

from adafruit_ble import BLERadio
from adafruit_ble.advertising.adafruit import AdafruitColor

# Define a list of tones/music notes to play.

c = [32, 65, 131, 262, 523]
db = [34, 69, 139, 277, 554]
d = [36, 73, 147, 294, 587]
eb = [37, 78, 156, 311, 622]
e = [41, 82, 165, 330, 659]
f = [43, 87, 175, 349, 698]
gb = [46, 92, 185, 370, 740]
g = [49, 98, 196, 392, 784]
ab = [52, 104, 208, 415, 831]
a = [55, 110, 220, 440, 880]
bb = [58, 117, 223, 466, 932]
b = [61, 123, 246, 492, 984]

# Star Wars Theme -- Key of C
starwars_notes = [c[3], g[3], f[3], e[3], d[3], c[4], g[3], f[3], e[3], d[3], c[4], g[3], f[3], e[3], f[3], d[3]]
starwars_beats = [4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4]

def playSong(songnotes, songbeats, tempo):
    '''
    songnotes: list of the melodies notes
    songbeats: list of melodies beat times
    tempo: speed of song, this is not traditional tempo in bpm like on a metronome,
        but more like a multiplier for whatever the notes are so a tempo value of 2
        make it play twice as fast. Adjust this by ear.

    This function plays the melody, simply by iterating through the list.
    '''
    print("Playing Song")
    for i in range(0, len(songnotes)):
        cp.play_tone(songnotes[i], songbeats[i]*tempo)


# The color pickers will cycle through this list with buttons A and B.
color_options = [0x110000,
                 0x111100,
                 0x001100,
                 0x001111,
                 0x000011,
                 0x110011,
                 0x111111,
                 0x221111,
                 0x112211,
                 0x111122]

ble = BLERadio()

i = 0
advertisement = AdafruitColor()
advertisement.color = color_options[i]
cpb.pixels.auto_write = False
cpb.pixels.fill(color_options[i])

while True:
    # The first mode is the color selector which broadcasts it's current color to other devices.
    if cpb.switch:
        print("Broadcasting color")
        ble.start_advertising(advertisement)
        while cpb.switch:
            last_i = i
            if cpb.button_a:
                i += 1
            if cpb.button_b:
                i -= 1
            i %= len(color_options)
            if last_i != i:
                color = color_options[i]
                cpb.pixels.fill(color)
                cpb.pixels.show()
                print("New color {:06x}".format(color))
                advertisement.color = color
                ble.stop_advertising()
                ble.start_advertising(advertisement)
                time.sleep(0.5)
        ble.stop_advertising()
    # The second mode listens for color broadcasts and shows the color of the strongest signal.
    else:
        closest = None
        closest_rssi = -80
        closest_last_time = 0
        print("Scanning for colors")

        while not cpb.switch:
            for entry in ble.start_scan(AdafruitColor, minimum_rssi=-100, timeout=1):
                if cpb.switch:
                    break
                now = time.monotonic()
                new = False
                if entry.address == closest:
                    pass
                elif entry.rssi > closest_rssi or now - closest_last_time > 0.4:
                    closest = entry.address
                else:
                    continue
                closest_rssi = entry.rssi
                closest_last_time = now
                discrete_strength = min((100 + entry.rssi) // 5, 10)
                cpb.pixels.fill(0x000000)
                print(entry.rssi)
                if entry.rssi > -40:  # trigger audio when VERY close.
                    playSong(starwars_notes, starwars_beats, .2)
                for i in range(0, discrete_strength):
                    cpb.pixels[i] = entry.color
                cpb.pixels.show()

            # Clear the pixels if we haven't heard from anything recently.
            now = time.monotonic()
            if now - closest_last_time > 1:
                cpb.pixels.fill(0x000000)
                cpb.pixels.show()
        ble.stop_scan()

