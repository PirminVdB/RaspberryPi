from zTryOut import raspberry
from time import sleep

if __name__ == '__main__':
    Board = raspberry.Board()
    Board.set_pin(1, 1, True)
    sleep(1)
    Board.set_pin(1, 2, True)
    Board.set_pin(1, 1, False)
    sleep(1)
    Board.reset()
    Board.set_pin(2, 1, True)
    sleep(1)
    Board.set_pin(2, 2, True)
    sleep(1)
    Board.set_pin(1, 1, True)