from RPi import GPIOS
import RPi.GPIO as GPIO

class Pins():
	pins = []
	def __init__(self):
		row1 = [GPIOS.gpio4 , GPIOS.gpio18]
		row2 = [GPIOS.gpio22, GPIOS.gpio25]
		self.pins.append(row1)
		self.pins.append(row2)

	def reset(self):
		GPIO.setmode(GPIO.BOARD)
		for pin in pins:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin,True)

	def start(self):

		print("gpio1on enzoverser")


class PinMapper():
	def get_pin(self, posX, posY):
		if posX<0 or posY<0:
			raise ValueError('De waarde voor posX of posY is kleiner dan 0. posX:%d, posY:%d' % (posX,posY)) #ValueError
		

if __name__ == '__main__':
	#LightTable().start()
	LightTable = LightTable()
	LightTable.init_pins()

