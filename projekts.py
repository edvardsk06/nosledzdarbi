from random import randint
 
jautajums = {
    "Latvijas": "Rīga","Lietuvas": "Viļņa","Igaunijas": "Tallina","Kenijas": "Nairobi","Polijas": "Varšava"
}
atslegas = list(jautajums.keys()) # parvers atslega spar list
print(atslegas)



skaits = 0
pareizas_atbildes = 0

while True:
    gadijums = randint(0, len(atslegas)-1)
    jaut = input(f"Kāda ir {atslegas[gadijums]} galvaspilsēta?")  # pajautā
    if jaut.lower() == "beigt":
        print("Paldies par spēli!")
        break
    elif jaut.capitalize()==jautajums[atslegas[gadijums]]:
        print("Pareizi!")
        pareizas_atbildes += 1
    else:
        print("Nepareizi!")
    skaits += 1
print(f"Tu pareizi atbildēji uz {pareizas_atbildes} no {skaits} jautājumiem!")







