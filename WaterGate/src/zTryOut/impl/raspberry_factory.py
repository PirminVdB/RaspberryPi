from src.zTryOut.impl import fake_raspberry

class BoardFactory():
    def get_board(self):
        return fake_raspberry.Board()