from time import sleep
from src.zTryOut.impl.raspberry_factory import BoardFactory

if __name__ == '__main__':
    Board = BoardFactory().get_board()
    Board.set_pin(0, 0, True)
    print(Board.get_pin_state(1, 1))
    sleep(1)
    Board.set_pin(0, 1, True)
    Board.set_pin(0, 0, False)
    sleep(1)
    Board.reset()
    Board.set_pin(1, 0, True)
    sleep(1)
    Board.set_pin(1, 1, True)
    sleep(1)
    Board.set_pin(0, 0, True)