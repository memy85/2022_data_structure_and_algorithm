#%% Abstract Data type

'''
Abstract data types are non-in-built data types. 
A programmer may define a new data type for his/her use. And these data types will have 
some operations. 

For this end, ADT are built.

* How to define ADT
- type of object -> class
- behaviour -> set of operations

By creating a ADT for our program/software, the programmer will have much easier way to
manipulate the data and focus on the algorithm.
'''

# ADT - List based Bag Implementation
'''
Lets develop a Bag ADT(Abstract data type)
- This is a container that stores a collection in which duplicate values are allowed
'''
#%%

class Bag :
    
    def __init__(self):
        self._theItems = list()
    
    def __len__(self):
        return len(self._theItems)
    
    def __contains__(self, item):
        return item in self._theItems
    
    def add(self, item):
        self._theItems.append(item)
        
    def remove(self, item):
        assert item in self._theItems, "The item must be in the bag."
        ndx = self._theItems.index(item)
        return self._theItems.pop(ndx)
    
    def __iter__(self):
        '''
        when called, returns an iterator object
        '''
        return _BagIterator(self._theItems)
        


class _BagIterator:
    '''
    An iterator for the Bag ADT
    '''
    def __init__(self, theList):
        self._bagItems = theList
        self.__curItem = 0
        
    def __iter__(self) :
        return self
    
    def __next__(self):
        if self.__curItem < len (self._bagItems):
            item = self._bagItems[self.__curItem]
            self.__curItem += 1
            return item
        else :
            raise StopIteration



#%%
my_bag = Bag()
my_bag.add(2)
my_bag.add(3)


#%%
# create BagIterator
iterator = my_bag.__iter__()

while True :
    try :
        item = iterator.__next__()
        print(item)
    
    except StopIteration :
        break


# Excercise 
#%% 
from time import time


class Time :
    def __init__(self, hour, minutes, seconds):
        self._absTime = 0
        assert self._isValidTime(hour, minutes, seconds), \
            "Invalid time format"
        '''
        absTime is based on second count
        '''
        self._absTime = hour * 60 * 60 + 60 * minutes + seconds
    
    def hour(self):
        hour = self._absTime // 60 * 60
        return hour
    
    def minutes(self):
        hour = self.hour()
        minutes = (self._absTime - hour * 60 * 60) // 60
        return minutes
    
    def seconds(self):
        hour = self.hour()
        minutes = self.minutes()
        seconds = self._absTime - hour * 60 * 60 - minutes * 60 
        return seconds 
    
    def numSeconds(self, otherTime):
        assert isinstance(otherTime, Time), "should be time instance"
        return abs(otherTime._absTime - self._absTime)
    
    def isAM(self):
        if self.hour() < 12 :
            return True
        else :
            return False
    
    def isPM(self):
        if self.hour() >= 12 :
            return True
        else :
            return False
    
    def comparable(self, otherTime):
        assert isinstance(otherTime, Time), "should be time instance"
        if self._absTime > otherTime._absTime :
            print("This is slower")
        elif self._absTime == otherTime._absTime :
            print("This is the same")
        else :
            print("This is faster")
            
        
    def to_string(self):
        print("%d2:%d2:%d2".format(self.hour(), self.minutes, self.seconds))
    
    def _isValidTime(self, hour, minute, second):
        if hour > 24 :
            return False
        if minute > 60 :
            return False
        if second > 60 :
            return False 
        else :
            return True
        

#%%
time1 = Time(1,20, 30)
time2 = Time(14, 30, 40)

