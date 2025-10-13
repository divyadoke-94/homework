class person:
    
    def __init__(self,name):
        self.name = name

class employee(person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary
#single ,#multiple ,


