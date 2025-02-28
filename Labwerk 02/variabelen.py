
'''
1. 
Schrijf een script met twee variabelen, name1 en age, waarin je je naam en leeftijd opslaat, het eerste als string, het tweede als integer. Print vervolgens deze informatie, zodat er bijvoorbeeld volgende output komt: 

>>> 

  Jony Christ – 33 years old 
2. 
Voeg één lijntje toe waardoor age met één wordt verhoogd, print opnieuw het resultaat. 
'''


name1 = (str(input("Enter your name: ")))
age1 = (int(input("Enter your age: ")) + 1)

print(f'{name1}  – {age1} years old')