import json

class Sucelje:
    def __init__(self, datoteka='adresar.json'):
        self.datoteka = datoteka
        try:
            with open(self.datoteka) as f:
                self.adresar = json.load(f)
        except FileNotFoundError:
            self.adresar = {}

    def dodaj_osobu(self, osoba, adresa):
        self.adresar[osoba.ime] = {
            'ime': osoba.ime,
            'prezime': osoba.prezime,
            'datum rodenja': osoba.datum_rodenja,
            'broj telefona': osoba.broj_telefona,
            'adresa': {
                'ulica': adresa.ulica,
                'broj': adresa.broj,
                'grad': adresa.grad,
                'postanski broj': adresa.postanski_broj,
                'drzava': adresa.drzava,
            }
        }

    def obrisi_osobu(self, ime):
        if ime in self.adresar:
            del self.adresar[ime]

    def ispis_kontakata(self):
        for osoba, podaci in self.adresar.items():
            print(f"{osoba}: {podaci}")

    def sacuvaj_adresar(self):
        with open(self.datoteka, 'w') as f:
            json.dump(self.adresar, f, indent=4)
