import random
current_score = 0
def dice(current_score):
    max_score=50
    min_value=1
    max_value=6
    throw = random.randint(min_value, max_value)
    if throw:
        if current_score >= max_score:
            print('Congratulations! You have reached 50 points.')
        elif throw == 1:
            print('You got a 1, Your new score is 0.')
            current_score = 0
            choice = input('Do you want to roll again? (y/n): ')
            if choice.lower() == 'y':
                dice(current_score)
            return current_score
        else:
            current_score += throw
            print('you got a ', throw)
            print('Your new score is ', current_score)
            choice = input('Do you want to roll again? (y/n): ')
            if choice.lower() == 'y':
                dice(current_score)

choice = input('Do you want to roll a dice? (y/n): ')
if choice.lower() == 'y':
    dice(current_score)

