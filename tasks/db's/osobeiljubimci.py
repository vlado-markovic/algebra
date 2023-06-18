from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Definiritati bazu podtaka
engine = create_engine('sqlite:///baza.db', echo=True)

# Povezat na tu bazu
Session = sessionmaker(bind=engine) # deklaracija klase
session = Session() # stvaranje objekta

# Trebamo nekako oznacit koje klase ce bit tablice
Base = declarative_base()

class Osoba(Base):
    __tablename__ = 'osobe'
    id = Column(Integer, primary_key = True)
    ime = Column(String)
    prezime = Column(String)
    god = Column(Integer)

class Ljubimac(Base):
    __tablename__ = 'ljubimci'
    id = Column(Integer, primary_key = True)
    ime = Column(String)
    pasmina = Column(String)
    # vlasnik_id =  Column(Integer, ForeignKey('osobe.id'))
    # def __init__(self, ime, pasmina): 
    # NE TREBA sqlalchemi za svoje klase sam definira init

vlasnistvo = Table('vlasnistvo', Base.metadata,
    Column('id_osobe', Integer, ForeignKey('osobe.id')),
    Column('id_ljubimca', Integer, ForeignKey('ljubimci.id'))
)
Osoba.ljubimci = relationship('Ljubimac', secondary= vlasnistvo, back_populates='vlasnici')
Ljubimac.vlasnici = relationship('Osoba', secondary= vlasnistvo, back_populates='ljubimci')

# Base.metadata.create_all(engine) # nadi sve tablice u kodu i stvori ih u enginu (bazi)

## CREAT
osoba1 = Osoba(ime= 'Igor', prezime= 'Vukas', god = 2000)
# session.add(osoba1)
# session.commit()

ljubimac1 = Ljubimac(ime='Bubi', pasmina='Pas')
ljubimac2 = Ljubimac(ime='Luci', pasmina='Macka')
# session.add_all([ljubimac1, ljubimac2])

# osoba1.ljubimci.extend([ljubimac1, ljubimac2])

# session.commit()

## READ
# get_all_people
# get_person_by_id
# get_people_by_name
# ....
def read_osoba_by_name(ime): 
    # u stvarnom kodu radili bi s ovom funkcijom i nju smestili u valstiti file za rad s bazom
    ljudi = session.query(Osoba).filter_by(ime= ime)
    return ljudi

ljudi = session.query(Osoba).all() # svi ljudi
# session (link) query(TABLICA) (tablica koji trazimo) .all() (svi)

for osoba in ljudi:
    print(osoba.prezime)

ljubimci = session.query(Ljubimac).filter_by(ime='Bubi') # ljubimci koji se zovu Bubi
for ljubimac in ljubimci:
    print(ljubimac.id, ljubimac.ime, ljubimac.pasmina)
    for vlasnik in ljubimac.vlasnici:
        print(vlasnik.ime)

## UPDATE
osoba = session.query(Osoba).filter_by(id=1).first() 
# dohvati sve s id 1 iz OSoba i onda uzmi prvog
osoba.ime = 'Pero' 
# prmijeni mu ime u Pero (ne treba posebn update zna da treba sam jer smo dohvatili sa sesson) 
session.commit()

## DELETE
macke = session.query(Ljubimac).filter_by(pasmina='Macka')
for macka in macke:
    session.delete(macka)
session.commit()