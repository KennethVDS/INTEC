'''
Oefening 7: Even of oneven 

 
1. 
Definieer een variabele number waarin je een natuurlijk getal stopt (= positieve integer). Schrijf code die nagaat of dit getal even is. 
Als dat zo is, wordt “even” geprint, indien niet gebeurt er niets. Tip: gebruik hiervoor de %-operator, a % b wil zeggen: “rest na deling van a door b”. 

2. 
Voeg aan het vorige code toe waardoor er “oneven” wordt geprint als het getal oneven is. 

3. 
In puntje 1 heb je allicht code geschreven die er als volgt uitziet: 
if <een voorwaarde>: 
           <doe iets> 
Voeg aan vorige code een lijntje toe waarbij je die voorwaarde opslaat in een variabele. Print deze. 

4. 
We maken een laatste variant. Nu krijg je niet het getal, maar een boolean die aangeeft of het getal even was of niet, bv. als eerste lijntje number_was_even = False. Schrijf opnieuw code die “even” of “oneven” print, afhankelijk van de waarde van number_was_even. 
Pro tip: doe dit zonder == te gebruiken in je if-statement! 
'''
number = int(input("Geef een natuurlijk getal: "))
number_was_even = bool(number % 2 == 0)
if number_was_even:
    print("even")
else:
    print("oneven")