class MyQueue(object):

    def __init__(self):
        self.s=[]
        self.s2=[]

    def push(self, x):
        self.s.append(x)
        

    def pop(self):
        for i in range(len(self.s)):
            self.s2.append(self.s.pop())
        popped=self.s2.pop()
        for i in range(len(self.s2)):
            self.s.append(self.s2.pop())
        return popped
        

    def peek(self):
        return self.s[0]
        

    def empty(self):
        if(len(self.s)==0):
            return True
        else:
            return False
        
