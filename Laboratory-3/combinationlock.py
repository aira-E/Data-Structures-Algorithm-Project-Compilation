class ComboLock:
    def __init__(self, secret1, secret2, secret3):
        self.secret1 = secret1
        self.secret2 = secret2
        self.secret3 = secret3

    def reset(self):
        reset = ComboLock(0,0,0)
        return reset
    
    def turnRight (self,ticks):
        self.secret1 = ticks
    
    def turnLeft(self,ticks):
        self.secret2 = ticks

    def AnotherturnRight (self,ticks):
        self.secret3 = ticks
      
#OpenTheLock
    def open (self):

        self.turnRight = int (input("Input number of ticks to right: "))
        self.turnLeft = int (input("Input number of ticks to left: "))
        self.AnotherturnRight  = int (input("Input another number of ticks to right: "))        
        if self.turnRight == lock.secret1 and self.turnLeft  == lock.secret2 and self.AnotherturnRight  == lock.secret3:  
            print ("The lock is opened!")
        else:
            print ("The lock is still locked!")
            lock.reset()

lock = ComboLock(38,16,22)
lock.open()




