'''
Oefening 8: Filmtoegang via geneste if’en  

1. Schrijf een functie movie_access() die twee parameters accepteert. De eerste is de leeftijd van de bezoeker. 
De tweede parameter is een Boolean die aangeeft of de film voor volwassenen is of niet. 
Implementeer het volgende flow chart met behulp van een geneste if-structuur (= een if-statement binnenin een ander if-statement). 
Je mag in je oplossing GEEN elif gebruiken. 

2. Schrijf nu een functie movie_access_alternate() die exact hetzelfde doet, maar dit keer door wel een elif-statement te gebruiken en geen geneste if.  

Meestal kan je een complexe if op de twee manieren schrijven (of zelfs een combinatie). 
Zolang je code correct functioneert maakt het niet uit wat je gebruikt, in de toekomst mag je dus kiezen. 
'''

def movie_access(age, adult):
    if adult:
        if age >= 18:
            print("Access granted")
        else:
            print("No adult movies for you kiddo")

    else: 
        print("Hope you enjoy your kiddo movie")
movie_access(22, True)  
    
    
def movie_access_alternate(age, adult):
    if age >= 18 and adult:
        print("Access granted")
    elif age < 18 and adult:
        print("No adult movies for you kiddo")
    elif adult == False:
        print("Hope you enjoy your kiddo movie")
movie_access_alternate(17, True) 