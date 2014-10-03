from enum import Enum
import RPi.GPIO as GPIO

class Pin(Enum):
    gpio4 = 7
    gpio17 = 11
    gpio18 = 12
    gpio21 = 13
    gpio22 = 15
    gpio23 = 16
    gpio24 = 18
    gpio25 = 22


class Board():
    pins = []
    def __init__(self):
        row1 = [Pin.gpio4 , Pin.gpio22]
        row2 = [Pin.gpio18, Pin.gpio25]
        self.pins.append(row1)
        self.pins.append(row2)
        self.reset()

    def reset(self):
        GPIO.setmode(GPIO.BOARD)
        for x in range(0,len(self.pins)):
            for y in range(0,len(self.pins[x])):
                GPIO.setup(self.get_pin(x, y).value, GPIO.OUT)
                self.set_pin(x, y, False)

    def set_pin(self, posX, posY, state):
        GPIO.output(self.get_pin(posX, posY).value,state)

    def get_pin(self, posX, posY):
        return self.pins[posX][posY]

    def clear(self):
        self.reset()
        GPIO.cleanup()
