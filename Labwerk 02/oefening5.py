'''

Oefening 5: Oppervlakte van de cirkel  

 
We maken een variant op oefening 2, je kan dus code van daar kopiëren. 
We zullen de eerste versie meer foolproof maken. Voorlopig is er immers niets om te vermijden dat een gebruiker een negatief getal ingeeft als straal, wat natuurlijk weinig betekenis heeft. 
Pas daarom de code aan: als de variabele radius positief is, wordt de oppervlakte en omtrek van de cirkel berekend en geprint, anders wordt een foutboodschap geprint, bv. “error – radius negative”. 
Beslis zelf waar je het geval onderbrengt waarbij de straal 0 is. (Men zou kunnen argumenteren dat een straal 0 niet zinnig is en een foutboodschap zou moeten opleveren, 
of evengoed dat dit een punt voorstelt, een cirkel met oppervlakte 0.) 

Het verschil is één teken. 
'''

radius= float(input("Enter the radius of the circle: "))
pi= float(3.141592653589793)
area=((radius**2)*pi)
circumference=(2*radius)*pi

if radius==0:
    print("error – radius is zero")

elif radius<0:
    print("error – radius negative")

else: 
    print(area)
    print(circumference)
