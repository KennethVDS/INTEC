'''
 Oefening 6: Uitgebreide begroeting of niet?  

Schrijf een functie greet_full_or_not() die twee parameters accepteert. 
De eerste is opnieuw de naam van de te groeten persoon. De tweede parameter is een Boolean die aangeeft of de begroeting al dan niet uitgebreid moet zijn. 
Indien niet (False) is de begroeting gewoon “Hello ”, indien wel (True) is de begroeting “Hello , I hope you have a pleasant day”.  

Je zou deze functie moeten kunnen schrijven zonder iets van de vorm == True of == False te schrijven in de if-structuur (!).  
'''
def greet_full_or_not(name, extended):
    if extended:
        print('Hello, I hope you have a pleasant day', name)
    else:
        print('Hello', name)
        
greet_full_or_not('Joy', True)  # Output: Hello, I hope you have a pleasant day Joy