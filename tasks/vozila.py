#Kreiranje fake baze
#ID je obicni cijeli broj
# podatci o svakom vozilu su: ID, tip, proiyvodac, reg, prva reg., cijena
vozilo1 = {
    'id' : 1,
    'tip' : 'Kamion',
    'proizvodac' : 'Iveco', 
    'rega' : 'OS 001 ZZ',
    'prva reg.' : 2015,
    'cijena' : 45000.00,
}
vozilo2 = {
    'id' : 2,
    'tip' : 'Tegljac',
    'proizvodac' : 'MAN', 
    'rega' : 'R1 001 ZZ',
    'prva reg.' : 2010,
    'cijena' : 90000.00,
}
vozilo3 = {
    'id' : 3,
    'tip' : 'Tegljac',
    'proizvodac' : 'Mercedes', 
    'rega' : 'ZG 001 ZZ',
    'prva reg.' : 2012,
    'cijena' : 95000.00,
}
vozilo4 = {
    'id' : 4,
    'tip' : 'Kombi',
    'proizvodac' : 'VW', 
    'rega' : 'RI 002 ZZ',
    'prva reg.' : 2021,
    'cijena' : 45000.00,
}
vozilo5 = {
    'id' : 5,
    'tip' : 'Kombi',
    'proizvodac' : 'Reno', 
    'rega' : 'ST 001 ZZ',
    'prva reg.' : 2021,
    'cijena' : 10000.00,
}
vozila = {
    1 : vozilo1,
    2 : vozilo2
}
vozila.update({3 : vozilo3}) # value moze biti bilo sta
vozila.update({4 : vozilo4})
vozila.update({5 : vozilo5})
# for i in range(5):
#     tip = input('Unesite tip vozima: ')
#     proizvodac = input("Unesite proizvodaca: ")
#     rega = input()
#     pr = input()
#     cj = input()
#     temp_vozilo = {
#         'id' : i+1,
#         'tip' : tip,
#         'proizvodac' : proizvodac, 
#         'rega' : rega,
#         'prva reg.' : pr,
#         'cijena' : cj,
#     }
#     print(temp_vozilo['id'])
#     vozila.update({i+1 : temp_vozilo})
# za ispis nam treba zaglavlje
# headers = ['ID', 'Tip', 'Proizvodac', 'Rega', 'God. pr.', 'Cijena']
print(vozila[1]['proizvodac'])
# for i in headers:
    # print(f'{i:^15}', end=' ')
print()
print('--------------------------------------------------------------------------------')
for vozilo in vozila.values():
    for key, value in vozilo.items(): 
        print(f'{value:^15}', end=' ')
    print()