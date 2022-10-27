
class Customer:
    def __init__(self):
        self.id
        self.firstName
        self.lastName
        self.company
        self.address
        self.city
        self.state
        self.zip
    
    def getfull_address(self):
        full_address=''
        
        if self.company=="":
            full_address+=self.firstName+" "+self.lastName+"\n"+self.address+"\n"+self.city+", " +self.state+" "+str(self.zip)
        else:
            full_address+=self.firstName+" "+self.lastName+"\n"+self.company+"\n"+self.address+"\n"+self.city+", " +self.state+" "+str(self.zip)
        return full_address
    
    