




print("Einfacher Taschenrechner")
print("========================")
#try block wird verwendet um Fehlerhafte werte aufzufangen
#beispiel user gibt statt einer zahl ein buchstaben ein
#ohne try catch würde das programm abstürzen und das wollen 
#gute programmierer um jeden preis verhindern
try:
    
    operator= input("Gib bitte deine Rechen art an +, -, *, / ")
    if operator == ["+","-","*","/"]:
        if operator == "+":
            zahl1 = float(input("gibt deine erste zahl ein"))
            zahl2 = float(input("bitte gib nun deine 2te zahl ein"))
            ergebnis = zahl1 + zahl2
            print(f"dein ergebniss ist = {ergebnis}")
        
        elif operator == "-":
            zahl1 = float(input("gibt deine erste zahl ein"))
            zahl2 = float(input("bitte gib nun deine 2te zahl ein"))
            ergebnis = zahl1 - zahl2
            print(f"dein ergebniss ist = {ergebnis}")
        
        elif operator == "*":
            zahl1 = float(input("gibt deine erste zahl ein"))
            zahl2 = float(input("bitte gib nun deine 2te zahl ein"))
            ergebnis = zahl1 * zahl2
            print(f"dein ergebniss ist = {ergebnis}")

        elif operator == "/":
            zahl1 = float(input("gibt deine erste zahl ein"))
            zahl2 = float(input("bitte gib nun deine 2te zahl ein"))
            if zahl2 or zahl2 !=0:
                ergebnis = zahl1 / zahl2
                print(f"dein ergebniss ist = {ergebnis}")
            else:
                print("nicht durch 0 teilen ")
        else:
            print("da ist was schief gegangen")

except TypeError:
    print("fehler nur zahlen oder gesagte operatoren eingeben !")
    