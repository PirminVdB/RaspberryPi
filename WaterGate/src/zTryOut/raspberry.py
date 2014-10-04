import abc

class Board(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def reset(self):
        return
    
    @abc.abstractmethod
    def set_pin(self, posX, posY, state):
        return
    
    @abc.abstractmethod
    def clear(self):
        return