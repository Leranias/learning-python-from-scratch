import random



print ("galgenmännchen")
print("===============")





wort_liste = [
    "programmierer",
    "sonnenblume",
    "autobahn",
    "tastatur",
    "python",
    "enwicklung"
    ]

geheimes_wort = random.choice(wort_liste).lower()
geratene_buchstaben = []
max_fehler = 7
aktuelle_fehler =0


#len kenne ich nicht könnte aber die wortlänge sein also len = lenght? wenn ja wird für die länge
#des wortes für jeden buchstaben ein - gesetzt
anzeige =["-"] *len(geheimes_wort)

#den vergleich mit aktuellen fehlern und maximal verstehe ich aber was hatt die anzeige länge damit zu tun ?
while aktuelle_fehler <max_fehler and "-" in anzeige:
    #\n is nen zeilen umbruch dann das plus verkettet oder fügt anzeige zusammen ? join is halt zusammenfügen oder beitreten heist 
    #inhalt aus anzeige wird dem print hinzugefügt in die leeren "" denke ich xD
    print("\n"+"".join(anzeige))
    #die zeile is auch nicht leicht mit den f können wir eine variabele einfach hinzufügen 
    # die '' anführungszeichen sehe ich relativ selten also scheinen sie etwas besonderes zu sein
    #zusätzlich join also verbinde  dann sorted  und die liste mit geratenen buchstaben heist 
    # verbinde eine sortierte liste von gertene buchstaben und gib sie mir aus ?
    print(f"bisher geratene Buchstaben: {', '.join(sorted(geratene_buchstaben))}")
    print(f"fehler: {aktuelle_fehler} von {max_fehler} maximalen fehlern ")

    eingabe = input("Rate einen Buchstaben: ").lower()
    #hier wird geschaut ob die länge der eingabe des nutzers auch wirklich einen einzigen buchstaben umfasst 
    #man könnte hier auch sagen oder prüfen ob das eingegebene wort das ziel wort ist oder nicht wenn nicht fehler
    #hier kam mir die idee eine prüfung einzubauen sowas wie
    # if eingabe == geheimes_wort: um den fall abzufrühstücken wenn der user das volle wort eingibt 
    #vieleicht hätte man auch parsen können wie ähnlich das wort zum ziel wort ist um schreib fehler 
    # ab zu fangen man müsste dann aber unter scheiden zwischen keksen und keks einzahl mehrzahl xD 

    if len(eingabe) != 1 or not eingabe.isalpha():
        print("ungültige eingabe bitte gib genau einen Buchstaben ein.")
        continue
    if eingabe in geratene_buchstaben:
        print("Diesen Buchstaben hast du schon geraten versuch einen anderen")
        continue
        
    geratene_buchstaben.append(eingabe)


    if eingabe in geheimes_wort:
        print(f"gut gemacht {eingabe} ist im wort enthalten")
        for index, buchstabe in enumerate(geheimes_wort):
            if buchstabe == eingabe:
                anzeige[index] = eingabe
    else:
        print(f"leider falsch {eingabe} ist nicht im wort")
        aktuelle_fehler +=1

print("\n ---Spielende---")
if "-" not in anzeige:
    print(f"du hast gewonnen das wort {geheimes_wort.upper()} erraten!")
else:
    print("leider verloren")
    print(f"das gesuchte wort war {geheimes_wort.upper()}")

