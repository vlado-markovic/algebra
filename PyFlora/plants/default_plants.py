import sys
sys.path.append('/home/vlado/Desktop/playground/algebra/PyFlora')


from src.orm import create_plant

media_folder = "PyFlora/plants/media"

plants = {
    
    "Dubrovačka zečina": { "image_path" : "dub_zecina.jpg" },
    "Pčelina kokica": { "image_path" : "pcelina_kokica.jpg" },
    "Patuljasti zvončić": { "image_path" : "patuljasti_zvoncic.jpg" },
    "Livadni procjepak ": { "image_path" : "livadni_procjepak.jpg" },
    "Učkarski zvončić": { "image_path" : "učkarski_zvončić.jpg" },
    "Jadranska perunika (Iris pseudopallida)": { "image_path" : "jadranska_perunika.jpg" },
    "Primorski vrisak (Satureja montana)": { "image_path" : "primorski_vrisak.jpg" },
    "Ljepljivi bušin (Cistus monspeliensis)": { "image_path" : "ljepljivi_bušin.jpg" },
    "Hrvatska sibireja (Sibiraea altaiensis subsp. croatica)": { "image_path" : "hrvatska_sibireja.jpg" },
    "Planinski božur (Paeonia mascula)": { "image_path" : "planinski_božur.jpg" },
    "Apeninska šumarica (Anemone apennina)": { "image_path" : "apeninska_šumarica.jpg" },
    "Proljetni jaglac (Primula auricula)": { "image_path" : "proljetni_jaglac.jpg" },
    "Gorocvijet (Adonis vernalis)": { "image_path" : "gorocvijet.jpg" },
    "Nar ili mogranj (Punica granatum) ": { "image_path" : "nar.jpg" }
    
}


for plant in plants:
    create_plant(plant, plant[0])
