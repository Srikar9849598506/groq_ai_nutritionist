
def user_number_check(user_number):

    if user_number <= 10:
        return "the user is just basic"
    elif user_number == 20:
        return "the user is advanced"
    elif user_number >= 30:
        return"the user is expert"
    else:
        return "enter the numbers from 10 to 30"