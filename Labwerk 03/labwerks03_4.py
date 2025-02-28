'''
Oefening 4: Begroeting op basis van lengte van de naam  

Je kan meer in een functie dan alleen maar tekst printen. 
Zo kan je er bijvoorbeeld een if-else-structuur aan toevoegen. 
Schrijf een functie greet_based_on_name_length() die een parameter name accepteert. 
De functie beslist op basis van de lengte van de naam welke begroeting geprint wordt:  

“Hello , you have quite a long name” of “Hello , you have a short name”. We beschouwen namen met minder dan 4 letters als “kort”.  
'''

def greet_based_on_name_length(name):
    if len(name) < 4:
        print('Hello, you have a short name')
    else:
        print('Hello, you have quite a long name')
        
# greet_based_on_name_length = lambda name: print('Hello, you have a short name' if len(name) < 4 else 'Hello, you have quite a long name') LAMBDA TIME

greet_based_on_name_length('Joy')  # Output: Hello, you have a short name