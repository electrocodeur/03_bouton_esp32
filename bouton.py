from machine import Pin

led = Pin(25, Pin.OUT)  # broche 25 en sortie
bp = Pin(26, mode=Pin.IN, pull=Pin.PULL_DOWN)


while True:
    if bp.value() == 1:
        led.value(1)   # allume la LED1
    else:
        led.value(0)   # éteint la LED1  


#bp = Pin(26, mode=Pin.IN, pull=Pin.PULL_DOWN)
#bp = Pin(26, mode=Pin.IN, pull=Pin.PULL_UP)
