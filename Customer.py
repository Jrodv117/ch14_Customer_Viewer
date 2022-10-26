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
            full_address+=self.firstName+" "+self.lastName+"\n"+self.address+"\n"+self.city+", " +self.state+" "+str(self.zip)
        else:
            full_address+=self.firstName+" "+self.lastName+"\n"+self.company+"\n"+self.address+"\n"+self.city+", " +self.state+" "+str(self.zip)
        return full_address
    
    