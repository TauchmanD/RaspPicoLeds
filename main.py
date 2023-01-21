import utime as time
import urequests as requests
import machine

import settings
from utils import connect_to_wifi, blikani, hex_to_rgb
from neopixel import Neopixel
from effects import Effects

NUMBER_OF_PIXELS = 150
BRIGHTNESS = 150
pixels = Neopixel(NUMBER_OF_PIXELS, 0, 28, "GRB")
effects = Effects(pixels)
pixels.brightness(BRIGHTNESS)


ACTIVE_ID: int = 0
ACTIVE_MODE: str = "00"

led = machine.Pin("LED", machine.Pin.OUT)
blikani()

connect_to_wifi()

time.sleep(2)

while True:
    led.on()
    r = requests.get("http://" + settings.DJANGO + "/api/leds/preset").json()
    led.off()
    new_id = r["id"]
    new_mode = r["mode"]
    color = hex_to_rgb(r["color"])
    if ACTIVE_ID != new_id:
        print(f"Preset changed (id) - {ACTIVE_ID} -> {new_id}")
        ACTIVE_ID = new_id
    if new_mode != ACTIVE_MODE:
        print(f"Mode changed - {ACTIVE_MODE} -> {new_mode}")
        ACTIVE_MODE = new_mode
    if ACTIVE_MODE == "CW":
        print("Color wipe")
        effects.color_wipe(color,0)
    elif ACTIVE_MODE == "SO":
        print("Solid color")
        effects.solid_color(color)
    elif ACTIVE_MODE == "RB":
        print("Duha")
        effects.rainbow_cycle(0)
    elif ACTIVE_MODE == "BR":
        print("Breathing")
        effects.breathing(color,0.1,BRIGHTNESS)
    elif ACTIVE_MODE == "TR":
        print("theater rainbow")
        effects.theater_chase_rainbow(0.1)
    elif ACTIVE_MODE == "MR":
        print("meteorite")
        effects.theater_chase_rainbow(color, 15, 2, 0.01)
    


