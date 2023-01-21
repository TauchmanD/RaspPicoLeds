import network
import secrets
import machine
import utime as time

led = machine.Pin("LED", machine.Pin.OUT)

def connect_to_wifi():
    print("Connecting...")
    led.on()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    time.sleep(10)
    if wlan.isconnected():
        print("Connected")
        return 1
    blikani()
    raise Exception


def blikani():
    for _ in range(5):
        led.on()
        time.sleep(0.3)
        led.off()
        time.sleep(0.3)

def hex_to_rgb(hex_color):
        h = hex_color.lstrip("#")
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

