def average(student_1, student_2, student_3, student_4, student_5):
    return (student_1 + student_2 + student_3 + student_4 + student_5) / 5

def got_zero(student_1, student_2, student_3, student_4, student_5):
    students = [student_1, student_2, student_3, student_4, student_5]
    for i in students:
        if i == 0:
            print(True)


def reward_class(average, got_zero):
    if got_zero:
        return "Too bad, no prize"
    elif not got_zero and average <= 12:
        return "Too bad, no prize"
    elif not got_zero and average > 12 and average <= 16:
        return "Free coupons"
    elif not got_zero and average > 16 and average < 20:
        return "Free dinner"
    elif average == 20:
        return "De ombudsman is verwittigd op verdenking van fraude"

def klastest():
    student_1 = 15
    student_2 = 18
    student_3 = 20
    student_4 = 17
    student_5 = 19

    avg = average(student_1, student_2, student_3, student_4, student_5)
    zero = got_zero(student_1, student_2, student_3, student_4, student_5)
    result = reward_class(avg, zero)
    
    print(f"Average: {avg}")
    print(f"Got zero: {zero}")
    print(f"Reward: {result}")

# Call the main function
klastest()