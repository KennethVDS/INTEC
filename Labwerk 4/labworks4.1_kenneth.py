'''
Oefening 1: Opwarmertje: Print vs Return 
1. 
Schrijf een functie average() die twee getallen als parameters neemt en het gemiddelde ervan print. 
Voer je functie uit met twee getallen naar keuze, om te checken of het resultaat klopt. 
2. 
Pas je functiedefinitie (Denk aan het verschil tussen definitie en aanroep!) 
nu aan zodat het resultaat niet meer wordt geprint, maar gereturned (gebruik het keyword return). 
Verander niets aan je functieaanroep! Wat gebeurt er als je je code uitvoert? 
3. 
Laat nu je functiedefinitie zoals ze was (met de return), maar zet een print rond je aanroep. 
Die zal er dus uitzien als print(average(6,8)) – maar natuurlijk met getallen naar keuze. 
Wat gebeurt er nu als je de code uitvoert? 
Het lijkt dus alsof returnen gewoon omslachtiger is dan printen, want je moet toch nog een print toevoegen om output te zien. 
Maar natuurlijk heeft returnen ook voordelen, die we proberen te demonstreren in de volgende oefening.'''
def average(a,b):
    return print((a+b)/2)

average(5,8)

'''
Oefening 2: Info delen tussen functies 
Dit code bevat twee functiedefinities: één die een lengte in inches omzet naar centimeter, 
en één die de totale prijs van een rol stof berekent op basis van de lengte (in cm) en de dikte van de stof. 
Het main-programma is voorlopig nog leeg. 

 
3. Sla het resultaat van de aanroep van inch_to_cm() op in een variabele met naam result. 

 
4. Gebruik deze variabele result nu als parameter in de aanroep van de functie 
calc_price(), in plaats van de centimeterwaarde. 
 

Voer je programma opnieuw uit. Als je alles correct hebt gedaan, zou je dezelfde prijs moeten krijgen als na stap 1. 
Dit betekent dat de acties die jij in stap 1 manueel hebt gedaan (functie uitvoeren, resultaat aflezen en invullen als parameter in de tweede functie)
nu automatisch zijn uitgevoerd door de computer. 
Dat is meteen ook de grote sterkte van een return: we kunnen vanaf nu informatie doorgeven van één functie naar een andere. 
'''
### function definition ### 

def inch_to_cm(inch_amount): 

    cm_amount = inch_amount * 2.54 

    return cm_amount

def calc_price(fabric_type, cm_amount): 

    if fabric_type == "thin": 

        price = 1.2 * cm_amount 

    else: 

        price = 3 * cm_amount 

    print( "the price is €", price ) 

   

### main program ### 
def main():
    inch_to_cm(20)
    calc_price("thin", 20)
main()