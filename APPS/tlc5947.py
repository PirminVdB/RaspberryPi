import time
import RPi.GPIO as GPIO

class GPIOOutput:
  def __init__(self, pin):
    self.pin = pin
    GPIO.setup(pin, GPIO.OUT)

  def high(self):
    self.__output(GPIO.HIGH)

  def low(self):
    self.__output(GPIO.LOW)

  def __output(self, type):
    GPIO.output(self.pin, type)

class TLC:
  def __init__(self, driver_count):
    self.clk = GPIOOutput(11)
    self.lat = GPIOOutput(8)
    self.dat = GPIOOutput(10)
    self.driver_count = driver_count
    self.lat.low()
    self.buffer = [0]*(24*driver_count)

  def __set_PWM(self, chan, pwm):
    if (pwm > 4095):
      pwm = 4095
    if (chan <= 24*self.driver_count):
      print("  set channel "+ str(chan) + " value: "+str(pwm))
      self.buffer[chan] = pwm

  def set_led(self, lednum, r, g, b):
    print("set led "+str(lednum)+" r:"+str(r)+" g:"+str(g)+" b:"+str(b))
    self.__set_PWM(lednum*3, r);
    self.__set_PWM(lednum*3+1, g);
    self.__set_PWM(lednum*3+2, b);

  def write(self):
    self.lat.low()
    for c in range((24*self.driver_count-1),-1,-1):
      for b in range(11, -1, -1):
        self.clk.low()
        if (self.buffer[c] & (1 << b)):
          self.dat.high()
        else:
          self.dat.low()
        self.clk.high()
    self.clk.low()
    self.lat.high()
    self.lat.low()
    time.sleep(1)

if __name__ == '__main__':
  try:
    GPIO.setmode(GPIO.BCM)
    TLC = TLC(1)
    for i in range(0,8):
      TLC.set_led(i, 0, 0, 4095)
      TLC.write()
    GPIO.cleanup()
  except KeyboardInterrupt:
    GPIO.cleanup()
