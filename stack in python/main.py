class Stack:
    
    maxsize=100
    items=[]
    
    
    def is_full(self):
        
        if len(self.items) == 0:
            
            return 1
        
        return 0
    
    def show(self):
        
        if self.is_full():
            print("full")
            
        else:
            
            for item in range(len(self.items)-1,-1,-1):
                print(self.items[item])
    
s1=Stack()

s1.show()