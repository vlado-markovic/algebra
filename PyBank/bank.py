import os
import datetime


def clear_screen():
    os.system('cls' if os.name == 'nt' else clear)
    
    
def generate(number):
    now = datetime.datetime.now()
    date_string = now.strftime('%Y-%m')
    broj = str(number).zfill(5)
    cont = "BA"