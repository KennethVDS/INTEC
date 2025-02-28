'''
Oefening 1: Begroeting op basis van een parameter  

De echte meerwaarde van functies zie je pas zodra je een parameter toevoegt. 
Herschrijf de definitie van de functie hello_function() zodat deze een parameter name accepteert, 
namelijk de naam van de te begroeten persoon. De functie verwerkt deze in de begroeting die geprint wordt. 
Bij de aanroep van de functie zal je dus ook een waarde moeten doorgeven als parameter. 
Je kan de functie ook meerdere keren oproepen in de “main” zodat je, in dit geval, ook meerdere personen kan begroeten. 
Je herhaalt de functie-aanroep met verschillende concrete waarden voor de parameter. Bovenaan je code blijft de functiedefinitie ongewijzigd. 
Controleer of je de juiste output krijgt:  

###main program### 

hello_function(‘Hannelora’) 

hello_function(‘Nigel’) 

Geprinte output in het shellvenster:  

>>> 

Hello Hannelora 

Hello Nigel '''

def hello_function(name): #Define the function with a parameter name
    print("Hello", name)  #body of the function
    
hello_function('Hannelora') #Call the function