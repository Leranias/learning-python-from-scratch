import os 

# hier wird die funktion erstellt um ein verzeichnis nach der gesuchten datei endung zu scannen
def scanne_verzeichniss(pfad,dateiendung):
    gefunden_dateien = []
    try:
        if not os.path.isdir(pfad):
            print(f"Fehler der angegebene pfad: {pfad} ist kein verzeichnis")
            return None
        
        alle_eintraege = os.listdir(pfad)


        for eintrag in alle_eintraege:
            voller_pfad =os.path.join(pfad,eintrag)
            if os.path.isfile(voller_pfad) and eintrag.endswith(dateiendung):
                gefunden_dateien.append(eintrag)

        return gefunden_dateien
    except FileNotFoundError:
        print(f"fehler der pfad: {pfad} wurde nicht gefunden!")
        return None
    except PermissionError:
        print(f"Fehler keine berechtigung um auf den pfad: {pfad} zuzugreifen")
        return None

#Haupt funktion die die anderen funktionen aufruft 
def main():
    print("----- Verzeichnis-Scanner----")
    #user gibt den pfad an beispiel C:\Users\Student\Desktop
    verzeichnis_pfad = input("Gib den Pfad zum verzeichnis ein das gescannt werden soll ")
    # hier kann der user seine endung angeben die er sucht 
    gesuchte_endung = input("Gib die datei endung an zb .txt oder .jpg")
    #hier wird die funktion aufgerufen und das was er findet in ergebnis gespeichert
    ergebnis = scanne_verzeichniss(verzeichnis_pfad,gesuchte_endung)
    #hier wird eine if abfrage genutzt um nur los zu legen wenn es nicht leer/none ist 
    if ergebnis is not None:
        print(f"\nSuche abgeschlossen in: {verzeichnis_pfad}")
        if not ergebnis:
            print(f"Keine Dateien mit der Endung: {gesuchte_endung} gefunden")
        else:
            print(f"gefundene Dateien mit der Endung: {gesuchte_endung}")
            for datei in ergebnis:
                print(f"= {datei}")

if __name__=="__main__":
    main()