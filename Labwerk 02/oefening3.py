'''
Definieer een variabele floor, die bijhoudt op welke verdieping een lift zich bevindt. 
Probeer ook eenseen negatief getal! Schrijf vervolgens code waardoor een belletje rinkelt als de lift zich op verdieping 55 bevindt. 
Het geluid van het belletje simuleren we door “DING!” te printen in het shellvenster. Voor andere waarden dan 55 gebeurt er niets. 
'''
import random
floor=(random.randint(-5,56))
if floor == 55:
        print("DING!")
#else:print("Lift is op verdieping", floor)

