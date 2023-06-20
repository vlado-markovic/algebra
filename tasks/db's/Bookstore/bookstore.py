from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Author, Publisher, Book, Base

# Kreiranje baze podataka i sesije
engine = create_engine('sqlite:///bookshop.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def main():
    print('Dobrodošli u Bookshop!')

    while True:
        print('\nOdaberite opciju:')
        print('1. Dodaj knjigu')
        print('2. Dodaj autora')
        print('3. Dodaj izdavača')
        print('4. Prikaži sve knjige')
        print('5. Prikaži sve autore')
        print('6. Prikaži sve izdavače')
        print('0. Izlaz')

        choice = input('Unesite opciju: ')

        if choice == '1':
            add_book()
        elif choice == '2':
            add_author()
        elif choice == '3':
            add_publisher()
        elif choice == '4':
            show_all_books()
        elif choice == '5':
            show_all_authors()
        elif choice == '6':
            show_all_publishers()
        elif choice == '0':
            break
        else:
            print('Pogrešan unos. Molimo pokušajte ponovno.')

    print('Hvala što ste posjetili Bookshop!')

def add_book():
    print('Unesite podatke o knjizi:')
    title = input('Naziv knjige: ')
    price = int(input('Cijena knjige: '))
    availability = int(input('Raspoloživost knjige: '))
    author_id = int(input('ID autora knjige: '))
    publisher_id = int(input('ID izdavača knjige: '))

    book = Book(title=title, price=price, availability=availability, author_id=author_id, publisher_id=publisher_id)
    session.add(book)
    session.commit()
    print('Knjiga je uspješno dodana!')

def add_author():
    print('Unesite podatke o autoru:')
    first_name = input('Ime autora: ')
    last_name = input('Prezime autora: ')

    author = Author(first_name=first_name, last_name=last_name)
    session.add(author)
    session.commit()
    print('Autor je uspješno dodan!')

def add_publisher():
    print('Unesite podatke o izdavaču:')
    name = input('Naziv izdavača: ')

    publisher = Publisher(name=name)
    session.add(publisher)
    session.commit()
    print('Izdavač je uspješno dodan!')

def show_all_books():
    books = session.query(Book).all()
    if books:
        print('Sve knjige:')
        for book in books:
            print(f'ID: {book.id}, Naziv: {book.title}, Cijena: {book.price}, Raspoloživost: {book.availability}')
    else:
        print('Nema dostupnih knjiga.')

def show_all_authors():
    authors = session.query(Author).all()
    if authors:
        print('Svi autori:')
        for author in authors:
            print(f'ID: {author.id}, Ime: {author.first_name}, Prezime: {author.last_name}')
    else:
        print('Nema dostupnih autora.')

def show_all_publishers():
    publishers = session.query(Publisher).all()
    if publishers:
        print('Svi izdavači:')
        for publisher in publishers:
            print(f'ID: {publisher.id}, Naziv: {publisher.name}')
    else:
        print('Nema dostupnih izdavača.')

if __name__ == '__main__':
    main()
