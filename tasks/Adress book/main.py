from sucelje.interface import Sucelje
from sucelje import unos

def start():
    sucelje = Sucelje()

    while True:
        opcija = unos.izbor_meni()
        
        if opcija == '1':
            osoba, adresa = unos.unesi_osobu()
            sucelje.dodaj_osobu(osoba, adresa)
            sucelje.sacuvaj_adresar()

        elif opcija == '2':
            ime = input('Unesite ime osobe koju želite obrisati: ')
            sucelje.obrisi_osobu(ime)
            sucelje.sacuvaj_adresar()

        elif opcija == '3':
            sucelje.ispis_kontakata()

        elif opcija == '4':
            print("Hvala na koristenju naseg servisa!")
            break

        else:
            print('Nepoznata opcija. Pokušajte ponovo.')

    


if __name__ == "__main__":
    start()