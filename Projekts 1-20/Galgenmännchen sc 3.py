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
    