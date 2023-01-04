class Stack:
    
    item=[]
    maxsize=100
    
    def is_full(self):
        
        if (len(self.item) == (self.maxsize)):
            
            return 1
        else:
            return 0
    
    
    def is_empty(self):
        
        if len(self.item) == 0:
            
            return 1
        else:
            
            return 0
            
    def push(self,x):
        
        if self.is_full():
            
            return None
        else:
            
            self.item.append(x)
            
    def show(self):
        
        if self.is_empty():
            
            return "stack in empty!!!!!"
        
        else:
        
            for item in range(len(self.item)-1,-1,-1):
            
                print(self.item[item])
    
    def peak(self):
        
        if self.is_empty():
            
            return "stack is empty!!!!1"
        
        else:
        
        
            return self.item[-1]
    
    def delete(self):
        
        
        if self.is_empty():
            
            return "stack is empty!!!!1"
        
        else:
            
            self.item.pop()
            

s1=Stack()

s1.push(55)
s1.push(45)
s1.push(75)
s1.push("mahdi")

s1.show()