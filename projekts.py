from tkinter import *
window = Tk()
window.title('Bilde')
window = Canvas(window,width= 1000, height = 900)
window.pack()
image = PhotoImage(file = 'C:\\Users\\Dators\\Desktop\\hist.png')
window.create_image(0,0, anchor = NW, image = image)
window.mainloop()


from random import randint
 
jautajums = {
    "Kad sākās Pirmais pasaules karš?Ieraksti gadu:": "1914",
    "Kurā gadā Džons F. Kenedijs tika noslepkavots?:": "1963",
    "Kur notika pirmās vasaras olimpiskās spēles?Ieraksti pilsētu:": "Atēnās",
    "Kurš bija pirmais amerikānis, kurš ieguva Nobela miera balvu?Ieraksti uzvārdu:": "Rūzvelts",
    "Kur atrodas Babilona?": "Irākā:",
    "Kur atrodas Žannas d'Arkas dzimtene? Ieraksti valsti:": "Francijā",
    "Kura notikuma laikā Koreja tika sadalīta 2 valstīs?:": "Otrā pasaules kara",
    "Kura tiek uzskatīta par pirmo cilvēka tehnoloģiju?:": "Uguns",
    "Kad sākās aukstais karš?:Ieraksti gadu": "1947",
    "Kura valsts Āzijā bija ass dalībniece Otrajā pasaules karā?:": "Japāna",
    "Kurš ir slavenais Kubas līderis, kuram pie varas bija 49 gadus?Ieraksti uzvārdu:": "Kastro",
    "Kurā okeānā nogrima Titāniks?Ieraksti vienu vārdu:": "Atlantijas",
    "Kurā gadā Latvija iestājās NATO:Ieraksti tikai gadu": "2004",
    "Kad tika parakstīta ASV Neatkarības deklarācija?Ieraksti tikai gadu:": "1776",
    "Kurā gadā notika Berlīnes mūra krišana?Ieraksti tikai gadu:": "1989",
    "Kurā gadā notika Bostonas tējas ballīte:Ieraksti tikai gadu:": "1773",
    "No kuras valsts bija Roalds Amundsens, kurš sasniedza Dienvidpolu?:": "Norvēģijas",
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


print("Pārbaudi zināšanas ar jā vai nē")
print("Pirmo laikrakstu pasaulē izveidoja Vācija.")
a = input()
if a.lower() == "jā":
    print("Pareizi")
else:
    print("Nepareizi")
    print("Pirmo laikrakstu pasaulē izveidoja Vācija")

print("Senajā Romā ir 7 dienas nedēļā.")
a = input()
if a.lower() == "jā":
    print("Nepareizi")
    print("Senajā Romā ir 8 dienas nedēļā.")
else:
    print("Pareizi")
    print("Senajā Romā ir 8 dienas nedēļā.")

print("Platons un Aristotelis bija grieķu filozofi.")
a = input()
if a.lower() == "jā":
    print("Pareizi")
    print("Abi bija grieķu filozofi.")
else:
    print("Nepareizi")
    print("Abi bija grieķu filozofi.")

print("Mumifikācija ir nākusi no Grieķijas.")
a = input()
if a.lower() == "jā":
    print("Nepareizi")
    print("Mumifikācija ir nākusi no Ēģiptes.")
else:
    print("Pareizi")
    print("Mumifikācija ir nākusi no Ēģiptes.")


print("Pirmais ASV prezidents bija Abrahams Linkolns.")
a = input()
if a.lower() == "jā":
    print("Nepareizi")
    print("Pirmais ASV prezidents bija Džordžs Vašingtons.")
else:
    print("Pareizi")
    print("Pirmais ASV prezidents bija Džordžs Vašingtons.")


print("Īslande bija pirmā valsts, kura atzina Latviju par neatkarīgu.")
a = input()
if a.lower() == "jā":
    print("Pareizi")
    print("Īslandes bija pirmā ārvalsts, kura 1991. gada 22. augustā apstiprināja Latvijas neatkarības atjaunošanu.")
else:
    print("Nepareizi")
    print("Īslandes bija pirmā ārvalsts, kura 1991. gada 22. augustā apstiprināja Latvijas neatkarības atjaunošanu.")
    print("Apsveicu, esi pabeidzis gatavošanās procesu, veiksmi eksāmenos!")

    
    
