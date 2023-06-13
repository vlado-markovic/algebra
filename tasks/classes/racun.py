#- Napravi klasu racun koja ima parametre:
#   param: broj racuna, datum izdavanja, lista artikala, ukupna cijena
#   funkcije:   izracun pdv-a, ispis racuna, dodaj artikal, obrisi artikal
#- neka artikal bude odvojena klasa sa (id, ime, cijena)
#- neka se cijena racuna iz ovih podataka

import datetime
import uuid

class Artikal:
    def __init__(self, ime, cijena, valuta="EUR"):
        self.id = str(uuid.uuid4())
        self.ime = ime
        self.cijena = round(cijena, 3)
        self.valuta = valuta


class Racun:
    brojac_racuna = 0 
    
    def __init__(self):
        Racun.brojac_racuna += 1
        self.broj_racuna = "R" + str(Racun.brojac_racuna).zfill(6)
        self.id = str(uuid.uuid4())
        self.datum_izdavanja = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.lista_artikala = []
        self.ukupna_cijena_artikala = 0.0

    def izracunaj_pdv(self):
        pdv = self.ukupna_cijena_artikala * 0.25  # PDV iznosi 25%
        return round(pdv, 3)

    def ukupni_iznos(self):
        return round(self.ukupna_cijena_artikala + self.izracunaj_pdv(), 3)
    
    def lista_kupljenih_artikala(self):
        return "".join([f"\n - {artikal.ime}: {artikal.cijena} {artikal.valuta} \n" for artikal in self.lista_artikala])

    def ispis_racuna(self):
        print(f"""
            ID: {self.id}      
            Racun broj: {self.broj_racuna}
            Datum izdavanja: {self.datum_izdavanja}
            Artikli:
            {self.lista_kupljenih_artikala()}
            Ukupna cijena: {round(self.ukupna_cijena_artikala, 3)} {self.lista_artikala[0].valuta}
            PDV: {round(self.izracunaj_pdv(), 3)} {self.lista_artikala[0].valuta}
            Ukupan iznos racuna: {round(self.ukupni_iznos(), 3)} {self.lista_artikala[0].valuta}
        """)

    def dodaj_artikal(self, artikal):
        self.lista_artikala.append(artikal)
        self.ukupna_cijena_artikala += artikal.cijena

    def obrisi_artikal(self, artikal):
        if artikal in self.lista_artikala:
            self.lista_artikala.remove(artikal)
            self.ukupna_cijena_artikala -= artikal.cijena
        else:
            print("Artikal ne postoji na racunu.")   


# Primjer korištenja
artikal1 = Artikal("Mlijeko", 2.5)
artikal2 = Artikal("Jogurt", 1.8,)
artikal3 = Artikal("Tubna", 3.77)
artikal4 = Artikal("Papir", 1.56)
artikal5 = Artikal("Jabuka", 4.2)
artikal6 = Artikal("Banana", 5.25)
artikal7 = Artikal("Ananas", 2.95)
artikal8 = Artikal("Kruh", 1.2)


racun = Racun()
racun.dodaj_artikal(artikal1)
racun.dodaj_artikal(artikal2)
racun.dodaj_artikal(artikal3)
racun.dodaj_artikal(artikal4)
racun.dodaj_artikal(artikal5)
racun.dodaj_artikal(artikal6)
racun.dodaj_artikal(artikal7)
racun.dodaj_artikal(artikal8)

racun.obrisi_artikal(artikal3)
racun.obrisi_artikal(artikal4)
racun.obrisi_artikal(artikal5)

racun.ispis_racuna()
