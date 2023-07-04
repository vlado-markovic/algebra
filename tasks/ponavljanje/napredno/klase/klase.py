import abc

class Helper():
    
    def get_screen_size():  # ovako se inace definiraju staticke funkcije, u klasama za posebno koristenje kasnije 
        pass

class Sizes():
    screen_size = 20
    small_Screen = 10

class FooClass(abc.ABC):
    def __init__(self, name) -> None:
        self.id = self.__generate_Id()
        self.name = name
        
    def __generate_Id(self):
        pass
    
    def sayHi(self):
        print (f"Hi {self.name}")
        
    def staticna_funkcija(): # i ovako se isto mogu koristit stat funkcije
        print("pozdrav svima")
        

class FooDijete(FooClass):
    def __init__(self, name) -> None:
        super().__init__(name)  




foo = FooClass("blabla")
foo.sayHi()

FooClass.staticna_funkcija() # staticku metodu moras pozvat na klasi