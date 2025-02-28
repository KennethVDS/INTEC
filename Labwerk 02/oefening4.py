'''
Oefening 4: Gebruikersnaam 

 
Definieer een variabele name waarin je een naam als string stopt. Om die te kunnen gebruiken als gebruikersnaam voor een website, moet die minstens 4 letters lang zijn. 
Schrijf daarom code die de variabele name overschrijft met twee keer de naam na elkaar als die te kort is.(We gaan ervan uit dat een naam sowieso minstens twee letters bevat.
Op deze manier is de verdubbelde naam wel minstens 4 lang.) 
 Zo zal “Ann” worden verlengd tot “AnnAnn”, “Jo” wordt “JoJo”, “Stef” blijft onveranderd. 
Print vervolgens de bekomen gebruikersnaam. Let op: print deze sowieso, of die nu verlengd moest worden of niet. 
Wat zou je moeten veranderen als je alleen de verlengde namen mag printen? Eén toets indrukken volstaat! 
Tip: je kan de lengte van een string vragen als len(<vul hier string in>). Probeer bijvoorbeeld eens print(len(<jouw naam>)). 
Tip: strings kan je aan elkaar plakken met +. Merk op dat de Python-interpreter zelf doorheeft hoe je + wil gebruiken: getallen optellen of strings samenvoegen, afhankelijk van het type van de argumenten. 
'''
name=str(input("Enter your name: "))

if len(name)<4:
    print(name*2)
else:
    print(name)
    
# indien er enkel de verdubbelde naam geprint mag worden, moet je de else weg laten.