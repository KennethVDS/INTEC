'''
Oefening 8: Lift 

 
1. 
We maken een iets complexere controlestructuur, in meerdere niveaus. 
We willen een lift programmeren voor een gebouw met 60 verdiepingen. Op basis van een variabele floor, die bijhoudt op welke verdieping de lift zich bevindt, moet het volgende gebeuren: 

• Op verdiepingen < 0 wordt een foutboodschap geprint: “error – lift te laag”; 
• Op verdiepingen > 60 wordt een foutboodschap geprint: “error – lift te hoog”; 
• Op verdiepingen 0 en 60 wordt “DING!” geprint; 
• Op verdiepingen die een veelvoud zijn van 10 (maar niet op 0 en 60) wordt het verdiepingnummer 
geprint; 
• Op alle andere verdiepingen gebeurt niets. 
Tip: een flowchart tekenen kan helpen bij deze opgave. 
Tip: “een veelvoud van 10” kan je nagaan met behulp van de %-operator. 
2. 
Herhaal de vorige voor een flatgebouw met 1000 verdiepingen. Dit is eenvoudig: je moet gewoon de code copy-pasten en op twee plaatsen de maximale verdieping aanpassen van 60 naar 1000. 
Maar wat als er op tien plaatsen in je code een voorwaarde zou staan die afhankelijk is van de hoogste verdieping? Of op honderd plaatsen? Dan zou je al deze voorkomens van 60 manueel moeten aanpassen naar 1000. Een betere aanpak is om je code generiek te maken door de hoogste verdieping op te slaan in een variabele (bv. genaamd max_floor), en op alle plaatsen waar er voorheen 60 stond nu deze variabele te gebruiken. Als de hoogste verdieping dan verandert, hoef je je code maar op één plaats aan te passen – de locatie waar je de variabele max_floor hebt gedefinieerd – ongeacht hoeveel keer je deze variabele 
in je code hebt gebruikt. 
Hou dit principe in de toekomst in gedachten. Als je meermaals dezelfde info nodig hebt, is het meestal te verkiezen om deze info op te slaan in een variabele in plaats van ze meermaals te copy-pasten. 

'''
import random
floor=(random.randint(-5,60))
if floor == 0 or floor == 60:
        print("DING!")
elif floor <0:
    print("error – lift te laag")
elif floor>60:
    print("error – lift te hoog")
else:
    if floor % 10 == 0 and floor!= 0 and floor!= 60:
        print("Lift is op verdieping", floor)


'''

import random
floor=(random.randint(-5,1000))
max_floor=1000
if floor == 0 or floor == max_floor:
        print("DING!")
elif floor <0:
    print("error – lift te laag")
elif floor>max_floor:
    print("error – lift te hoog")
else:
    if floor % 10 == 0 and floor!= 0 and floor!= max_floor:
        print("Lift is op verdieping", floor)

'''