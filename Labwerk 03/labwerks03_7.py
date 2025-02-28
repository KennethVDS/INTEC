'''
Oefening 7: Alcoholcontroles  

De Leuvense politie wil dit jaar zwaar inzetten op het controleren van dronken fietsers. 
De boetes worden hoger naarmate het alcoholpercentage in je bloed. 
Bedenk een oplossing om de te betalen boete te berekenen voor een gegeven alcoholpercentage. 
Schrijf een functie calculate_fine() die de boete in de Shell print op basis van 
het geblazen alcoholpercentage, dat je doorgeeft als parameter: 

• VVV Alcoholpercentage < 0.5‰ : geen boete  
• Op schijf 0.5‰ tot en met 0.8‰: €50 boete  
• Op schijf groter dan 0.8‰ tot en met 1.5‰: de boete stijgt lineair vanaf €50 bij 0.8‰ tot €150 bij 1.5‰. 
 
• Als alcoholpercentage > 1.5‰: €250 boete en geprinte boodschap: “you are in mortal danger”  
• VVV Als er een foutieve (negatieve) waarde wordt ingegeven: “Error, negative value detected”

Je kan de volgende formule gebruiken om in dit geval de boete te berekenen2 : 50 + (((alcoholpercentage - 0.8) / 0.7) * 100) 

In deze regels wordt het alcoholpercentage uitgedrukt in promille, in je code kan je dit vertalen naar een float: 0.5‰ wordt simpelweg het getal 0,5. Let op, de komma bij decimalen is een punt in Python.
'''

def calculate_fine(alcohol_percentage):
    if alcohol_percentage < 0:
        print('Error, negative value detected')
    elif alcohol_percentage < 0.5:
        print('No fine')
    elif alcohol_percentage <= 0.8:
        print('€50 fine')
    elif alcohol_percentage <= 1.5:
        fine = 50 + (((alcohol_percentage - 0.8) / 0.7) * 100)
        print(fine, 'fine')
    elif alcohol_percentage > 1.5:
        print('€250 fine and you are in mortal danger')
            
            
calculate_fine(0.9)
