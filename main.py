from machine import Pin
from utime import sleep

switchselline1 = Pin(15, Pin.IN)
switchselline2 = Pin(16, Pin.IN)
switch1 = Pin(25, Pin.IN)
switch2 = Pin(26, Pin.IN)
switch3 = Pin(27, Pin.IN)
switch4 = Pin(12, Pin.IN)
led = Pin(5, Pin.OUT)

while True:
    valueS1 = switch1.value()
    valueS2 = switch2.value()
    valueS3 = switch3.value()
    valueS4 = switch4.value()
    if switchselline1.value() == 0 and switchselline2.value() == 0:
        led.value(valueS1)
    elif switchselline1.value() == 1 and switchselline2.value() == 0:
        led.value(valueS2)
    elif switchselline1.value() == 0 and switchselline2.value() == 1:
        led.value(valueS3)
    elif switchselline1.value() == 1 and switchselline2.value() == 1:
        led.value(valueS4)
    sleep(0.5)