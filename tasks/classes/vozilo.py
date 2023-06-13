# Napraviti abstraktnu klasu vozilo 
# i njene pod klase motor, kamion, avion 

from abc import ABC, abstractmethod

class Vozilo(ABC):
    def __init__(self, naziv, brzina):
        self.naziv = naziv
        self.brzina = brzina
    
    @abstractmethod
    def pokreni(self):
        pass
    
    @abstractmethod
    def zaustavi(self):
        pass

class Motor(Vozilo):
    def __init__(self, naziv, brzina, obujam_motora):
        super().__init__(naziv, brzina)
        self.obujam_motora = obujam_motora
    
    def pokreni(self):
        print(f"{self.naziv} je pokrenut.")
    
    def zaustavi(self):
        print(f"{self.naziv} je zaustavljen.")
        
    def informacije_vozila(self):
        print(f"naziv vozila: {self.naziv}, brzina: {self.brzina}, obujam_motora: {self.obujam_motora}")

class Kamion(Vozilo):
    def __init__(self, naziv, brzina, nosivost, obujam_motora):
        super().__init__(naziv, brzina)
        self.nosivost = nosivost
        self.obujam_motora = obujam_motora
    
    def pokreni(self):
        print(f"{self.naziv} je krenuo.")
    
    def zaustavi(self):
        print(f"{self.naziv} je zaustavljen.")
        
    def informacije_vozila(self):
        print(f"naziv vozila: {self.naziv}, nosivost vozila: {self.nosivost}, obujam_motora: {self.obujam_motora}")

class Avion(Vozilo):
    def __init__(self, naziv, brzina, visina):
        super().__init__(naziv, brzina)
        self.visina = visina
    
    def pokreni(self):
        print(f"{self.naziv} je poletio.")
    
    def zaustavi(self):
        print(f"{self.naziv} je sletio.")
        
    def informacije_vozila(self):
        print(f"naziv vozila: {self.naziv}, brzina vozila: {self.brzina}, visina: {self.visina}")


motor = Motor("Motor 1", 100, 1500)
motor.pokreni()  
motor.zaustavi() 
motor.informacije_vozila()

kamion = Kamion("Kamion 1", 80, 5000, 10000)
kamion.pokreni()  
kamion.zaustavi() 
kamion.informacije_vozila() 

avion = Avion("Avion 1", 500, 10000)
avion.pokreni() 
avion.zaustavi()
avion.informacije_vozila() 
