'''
Oefening 6: Oppervlakte van de cirkel  

 
We maken een derde variant. Voeg daarom een eerste check toe die controleert of pi wel exact genoeg is. Waarden 3 of 3.1 zijn niet exact genoeg.
Als de variabele pi gelijk is aan één van deze twee, wordt een foutboodschap geprint, bv. “error – pi not exact enough”. 
Als pi wel exact genoeg gekend is, wordt opnieuw het vorige onderscheid gemaakt: positieve straal levert de oppervlakte, negatieve een geprinte foutboodschap. 
Merk op dat onze check voor de exactheid van pi eigenlijk heel naïef is: alle andere waarden dan 3 en 3.1 worden als “exact genoeg” beschouwd, dus ook totaal andere getallen. 
Later dit semester kan je betere algoritmes proberen bedenken om de nauwkeurigheid van pi te berekenen, maar voorlopig houden we het bij deze eenvoudige aanpak. 
Tip: gebruik ergens elif.  
'''
radius= float(input("Enter the radius of the circle: "))
pi= 3.1
area=((radius**2)*pi)
circumference=(2*radius)*pi

if radius>=0:
    if pi==3 or pi == 3.1:
        print("error – pi not exact enough")
    else:
        print(area)
        print(circumference)
else:
    print("error – radius negative or zero")