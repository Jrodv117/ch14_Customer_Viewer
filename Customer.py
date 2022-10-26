from dataclasses import dataclass

@dataclass

class Customer:
    id:int
    firstName:str
    lastName:str
    company:str
    address:str
    city:str
    state:str
    zip:int
    
    def getfull_address(self):
        full_address=''
        
        if self.company=="":
            full_address+=self.firstName+" "+self.lastName+"\n"+self.address
            
        
    
    