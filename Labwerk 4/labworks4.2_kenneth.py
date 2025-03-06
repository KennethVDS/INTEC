
'''
• Schrijf een main-programma waarin je eerst de functie F_to_C() gebruikt om een 
bepaalde temperatuur in Fahrenheit om te zetten naar Celsius en de returnwaarde 
opslaat in een variabele temp_converted_to_C. Gebruik deze variabele vervolgens 
als parameter voor een aanroep van alert_user(). Sla ook de returnwaarde van deze 
functie op in een variabele en print deze ten slotte (als je dit laatste niet doet zal je 
geen output zien).
'''

def F_to_c(fahrenheit):
    teveelkommas = (fahrenheit - 32) / 1.8
    celcius = round(teveelkommas, 2)
    return celcius

def alert_user(celcius):
    if celcius > 100:
        return "Water boiling"
    elif 85 <= celcius <= 90:
        return "Ready to make tea"
    elif 40 <= celcius <= 45:
        return "Perfect for a foot bath"
    else:
        return f"Current water temperature is {celcius}°C"
    
def main(temperatuur):
    temp_converted_to_C = F_to_c(temperatuur)
    alert = alert_user(temp_converted_to_C)
    print(alert)
    
main(177)