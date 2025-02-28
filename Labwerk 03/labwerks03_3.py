'''
Oefening 3: Oppervlakte van de cirkel als functie  

In labwerk 2 schreef je de code om de oppervlakte van een cirkel te berekenen en te printen. 
Je had toen nog niet geleerd om met functies en functieparameters te werken. 
Schrijf een functie calculate_area() die met de straal van de cirkel als parameter de oppervlakte van een cirkel berekent 
en print in de Shell wanneer je in de main de functie op de volgende manier oproept: calculate_area(10)  

Merk op dat je de (afgeronde) waarde van pi niet doorgeeft als parameter!  
'''
radius= float(input("Enter the radius of the circle: "))
def calculate_area(radius):
    pi= 3.14
    area=((radius**2)*pi)
    circumference=(2*radius)*pi

    if radius>=0:
        if pi==3 or pi == 3.1:
            print("error – pi not exact enough")
        else:
            print('de oppervlakte van de cirkel is ', area)
            print('de omtrek van de cirkel is ', circumference)
    else:
        print("error – radius negative or zero")
        
calculate_area(radius)