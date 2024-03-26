from random import randint
 
jautajums = {
    "Kad sākās Pirmais pasaules karš?": "1914",
    "Kurā gadā Džons F. Kenedijs tika noslepkavots?": "1963",
    "Kur notika pirmās vasaras olimpiskās spēles?Ieraksti pilsētu": "Atēnās",
    "Kurš bija pirmais amerikānis, kurš ieguva Nobela miera balvu?Ieraksti uzvārdu": "Rūzvelts",
    "Kur atrodas Babilona?": "Irākā",
    "Kur atrodas Žannas d'Arkas dzimtene? Ieraksti valsti": "Francijā",
    "Kura notikuma laikā Koreja tika sadalīta 2 valstīs?": "Otrā pasaules kara",
    "Kura tiek uzskatīta par pirmo cilvēka tehnoloģiju?": "Uguns",
    "Kad sākās aukstais karš?": "1947",
    "Kura valsts Āzijā bija ass dalībniece Otrajā pasaules karā?": "Japāna",
    "Kurš ir slavenais Kubas līderis, kuram pie varas bija 49 gadus?Ieraksti uzvārdu": "Kastro",



}
atslegas = list(jautajums.keys()) # parvers atslega spar list
# print(atslegas)

skaits = 0
pareizas_atbildes = 0
print("Sagatavojoies Vēstures eksāmenam! Lai spēli beigtu, lodziņā uzraksti 'beigt'")
while True:
    gadijums = randint(0, len(atslegas)-1)
    jaut = input(f" {atslegas[gadijums]}")  # pajautā
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







