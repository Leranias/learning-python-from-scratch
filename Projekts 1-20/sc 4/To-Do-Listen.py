import json
import os


#festlegung des datei namens. warum wird das vollständig groß geschrieben ? 
DATEINAME = "todoliste.json"

def lade_aufgaben():
    if not os.path.exists(DATEINAME):
        return []
    
    try:
        with open(DATEINAME,"r", encoding="utf-8") as datei:
            return json.load(datei)
       
    except json.JSONDecodeError:
        return []
#aufgaben speichern
def speichere_aufgaben(aufgaben):
    with open(DATEINAME,"w", encoding= "utf-8")as datei:
        json.dump(aufgaben,datei,indent = 4)

#aufgaben anzeigen
def zeige_aufgaben(aufgaben):
    print("\n--- deine TO-Do-liste ---")
    if not aufgaben:
        print("du hast noch keine aufgaben klasse")

    else:
        for index, aufgabe in enumerate(aufgaben, 1):
            status = "x" if aufgabe["erledigt"] else""
            print(f"{index}. [{status}] {aufgabe['text']}")
    print("--------------------------")
#aufgaben hinzufügen
def fuege_aufgabe_hinzu(aufgaben):
    text = input("gib den text der neuen aufgabe ein: ")
    neue_aufgabe ={"text": text, "erledigt": False}
    aufgaben.append(neue_aufgabe)
    speichere_aufgaben(aufgaben)
    print(f"Aufgabe '{text}' hinzugefügt")
#Hier werden aufgaben als erledigt markiert
def markiere_als_erledigt(aufgaben):
    zeige_aufgaben(aufgaben)
    try:
        nummer= int(input("gib die nummer der aufgabe ein die du erledigt hast"))
        if 1 <= nummer <= len(aufgaben):
            aufgaben[nummer-1]["erledigt"]=True
            speichere_aufgaben(aufgaben)
            print("aufgabe als erledigt markiert")
        else:
            print("ungültige nummer")    
    except ValueError:
        print("bitte gib eine gültige zahl ein.")
##Hauptfunktion mit auswahl menü und if abfragen zur auswahl
def main():
    aufgaben = lade_aufgaben()
    while True:
        print("\nmenü")
        print("1. aufgaben anzeigen")
        print("2. aufgabe hinzufügen")
        print("3. aufgaben als erledigt markieren")
        print("4.beenden")

        auswahl = input("wähle eine option: ")

        if auswahl == "1":
            zeige_aufgaben(aufgaben)
        elif auswahl =="2":
            fuege_aufgabe_hinzu(aufgaben)
        elif auswahl =="3":
            markiere_als_erledigt(aufgaben)
        elif auswahl == "4":
            print("programm wird beendent")
            break
        else:
            print("ungültige auswahl")

# hauptfunktions aufruf
if __name__=="__main__":
    main()