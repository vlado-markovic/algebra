class Automobil:
    def __init__(self, obujam_motora, snaga_motora, maksimalna_brzina, boja, proizvodac, model, godiste, vozno_stanje):
        self.obujam_motora = obujam_motora
        self.snaga_motora = snaga_motora
        self.maksimalna_brzina = min(maksimalna_brzina, 200)  # Ensure maksimalna_brzina is not greater than 200
        self.boja = boja
        self.proizvodac = proizvodac
        self.model = model
        self.godiste = godiste
        self.vozno_stanje = vozno_stanje
    
    def voziti(self, brzina):
        if self.vozno_stanje != "ne vozi" and brzina <= self.maksimalna_brzina and brzina > 0:
            print(f"Automobil {self.proizvodac} {self.model} vozi brzinom od {brzina} km/h.")
        elif self.vozno_stanje == "ne vozi":
            print("Automobil se ne može voziti jer je u stanju 'ne vozi'.")
        else:
            print(f"Nemoguće postići brzinu od {brzina} km/h.")
    
    def zaustaviti(self):
        print(f"Automobil {self.proizvodac} {self.model} je zaustavljen.")
    
    def pokvario_se(self):
        self.vozno_stanje = "ne vozi"
        print(f"Automobil {self.proizvodac} {self.model} se pokvario i sada se ne može voziti.")
    
    def popravi_se(self):
        self.vozno_stanje = "odlicno"
        print(f"Automobil {self.proizvodac} {self.model} je popravljen i u odličnom stanju.")
    
    def promjeni_stanje(self, novo_stanje):
        print (self.maksimalna_brzina)
        self.vozno_stanje = novo_stanje
        print(f"Stanje automobila {self.proizvodac} {self.model} je promijenjeno u '{novo_stanje}'.")


# Create an instance of Automobil class
automobil = Automobil(
    obujam_motora=input("Unesite obujam motora: "),
    snaga_motora=input("Unesite snagu motora: "),
    maksimalna_brzina=int(input("Unesite maksimalnu brzinu: ")),
    boja=input("Unesite boju: "),
    proizvodac=input("Unesite proizvođača: "),
    model=input("Unesite model: "),
    godiste=input("Unesite godište: "),
    vozno_stanje=input("Unesite vozno stanje: ")
)

# Use the methods of the instance
automobil.voziti(brzina=250)
automobil.zaustaviti()
automobil.pokvario_se()
automobil.popravi_se()
automobil.promjeni_stanje(novo_stanje="ok")
