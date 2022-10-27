
from audioop import add
from os import stat


class Customer:
    def __init__(self, id, firstName, lastName, company, address, city, state, zip):
        self.cust_id=id
        self.first_name=firstName
        self.last_name=lastName
        self.company=company
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        
    
    
    def __str__(self):
        full_address=''
        
        if self.company=="":
            full_address+=self.first_name+" "+self.last_name+"\n"+self.address+"\n"+self.city+", " +self.state+" "+str(self.zip)
        else:
            full_address+=self.first_name+" "+self.last_name+"\n"+self.company+"\n"+self.address+"\n"+self.city+", " +self.state+" "+str(self.zip)
        return full_address
    
    