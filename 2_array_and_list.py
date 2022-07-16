from functools import reduce

class Array:
    
    def __init__(self):
        self.value = list()
    
    def sum(self):
        result = map(sum,self.value)
        return result
    