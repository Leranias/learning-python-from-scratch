import random








while True:



    versuche = 3

    while versuche > 1:
        try:
            print("willkomen beim zahlen raten")
            spielModusAuswahl = input("willst du selber wählen wie hoch du raten willst ? ja/nein").lower()

            if spielModusAuswahl =="ja":
                unterezahl = int("gib die niedrigste oder kleinste zahl ein ")
                höchstezahl =int("gib nun die höchste zahl oder das maximum ein ")
                zahlenraten(unterezahl,höchstezahl)



                
            


        



    def zahlenraten(min,max):
       randomzahl = random.randint(min,max)
        
       
    
    