'''
Oefening 5: Begroeting op basis van lengte van de naam, als parameter  

Pas de functie van oefening 4 aan zo dat je kan beslissen welke lengte je als “kort” beschouwt. 
'''


def greet_based_on_name_length(name, length):
    if len(name) < length:
        print('Hello, you have a short name')
    else:
        print('Hello, you have quite a long name')
        
# greet_based_on_name_length = lambda name: print('Hello, you have a short name' if (len(name) < 4 length) else 'Hello, you have quite a long name') LAMBDA TIME

greet_based_on_name_length('Joy', 4)  # Output: Hello, you have a short name