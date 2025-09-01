import random



#funktion die das zahlen raten darstellt
#ich wollte sie eigendlich unten in code platzieren aber 
#wollte python nicht weil unnereichbar was sinn macht aber
#aus c# bin ich das etwas anders gewohnt

def zahlenraten(min,max):
    
    #hier holen wir uns die übergebenen parameter und nutzen sie als min und max wert 
    randomzahl = random.randint(min,max)    
    versuche = 3
    #spiele schleife
    while versuche >0:
        try:
            gerateneZahl = int(input("dann Rate mal los bitte deine zahl eingeben: = "))
            
            # das eigendliche spiel beginnt hier
            if gerateneZahl == randomzahl:
                print(f"WOW du hast die zahl erraten deine zahl war {randomzahl} un glaublich!! ")
                break
            
            elif gerateneZahl < randomzahl:
                print("Zu Klein !")
                versuche -= 1
            elif gerateneZahl > randomzahl:
                print("Zu Hoch! ")
                versuche -= 1
            else:
                print("öö wie zum teufel  bist du hier hin gekommen ? husch ins körpchen ")
                break

        except ValueError:
            print("bitte gib eine zahl an wird neugestartet ")
            break


#Hauptanwendungs code
while True:
    #fall back und standart zahlen zum raten
    unterezahl = 1
    höchstezahl = 10
    
    try:
        #auswahl ob man selber die zahlen wählen zu können
        print("willkomen beim zahlen raten")
        spiel_Modus_Auswahl_Zahlenraten = input("willst du selber wählen wie hoch du raten willst? ja/nein: ").lower()

        if spiel_Modus_Auswahl_Zahlenraten == "ja":
            unterezahl = int(input("gib die niedrigste oder kleinste zahl ein "))
            höchstezahl = int(input("gib nun die höchste zahl oder das maximum ein "))
            zahlenraten(unterezahl,höchstezahl)
            
        else:
            
            print("standart also gut dann 1 bis 10")
            zahlenraten(unterezahl,höchstezahl)
    except TypeError:
        print("fehler")


    print("SPIEL ENDE!!!")
    auswahl = input("willst du weiter spielen ja/nein ").lower()
    if auswahl =="nein":
        break