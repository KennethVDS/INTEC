'''
Oefening 2: Begroeting op basis van twee parameters  

Een functie kan ook meer dan één parameter hebben. 
Schrijf een functie hello_to() die twee parameters accepteert. 
De eerste is opnieuw de naam van de te begroeten persoon. 
De tweede parameter is de plaats waar we de persoon begroeten. 
Zo zou de functie-oproep  

hello_to( “Stef”, “Group T” )  

de geprinte output moeten geven:  

Hello Stef, and welcome to Group T.  

Je kan op twee manieren tekst aan elkaar plakken: print( “tekst”, “nog tekst” ) zal de twee delen printen, gescheiden door een spatie. print( “tekst” + “nog tekst” ) zal de strings aaneen plakken (zonder spatie) en printen.  
'''
def hello_to(name, place):                                          #define the function with two parameters name and place
    print('Hello', name, ', and welcome to', place + '.')           #body of the function
    
hello_to('kenneth', 'Intec')                                        #Call the function