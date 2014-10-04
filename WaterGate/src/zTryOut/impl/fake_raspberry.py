from src.zTryOut import raspberry

class Board(raspberry.Board):
    pins = []
    def __init__(self):
        self.pins = [[0,0],[0,0]]
    
    def reset(self):
        for x in range(0,len(self.pins)):
            for y in range(0,len(self.pins[x])):
                self.pins[x][y] = 0
        return

    def set_pin(self, posX, posY, state):
        self.pins[posX][posY] = state
        return

    def get_pin_state(self, posX, posY):
        return self.pins[posX][posY]

    def clear(self):
        return

