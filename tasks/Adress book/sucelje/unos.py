from osoba.Osoba import Osoba
from adresa.Adresa import Adresa
# from sucelje import interface/

def unesi_osobu():
    ime = input('Unesite ime osobe: ')
    prezime = input('Unesite prezime osobe: ')
    datum_rodenja = input('Unesite datum rođenja osobe (format DD.MM.GGGG.): ')
    broj_telefona = input('Unesite broj telefona osobe: ')
    osoba = Osoba(ime, prezime, datum_rodenja, broj_telefona)

    ulica = input('Unesite ulicu adrese osobe: ')
    broj = input('Unesite broj adrese osobe: ')
    grad = input('Unesite grad adrese osobe: ')
    postanski_broj = input('Unesite poštanski broj adrese osobe: ')
    drzava = input('Unesite državu adrese osobe: ')
    adresa = Adresa(ulica, broj, grad, postanski_broj, drzava)

    return osoba, adresa

def izbor_meni():
    print('\nIzaberite opciju:')
    print('1. Dodaj osobu')
    print('2. Obriši osobu')
    print('3. Ispisi sve kontakte')
    print('4. Izlaz')

    opcija = input('Vaš izbor: ')
    return opcija
