
def variable_concept():
    user_age = 27
    user_height = 5.6
    user_name = "theprakash97"
    GENDER = 'M'
    is_active_now = False

    print(user_age)
    print(user_height)
    print(user_name)
    print(GENDER)
    print(is_active_now)

    print()

    # assignment
    user_age = 30
    print(user_age)
    user_age *= 2
    print(user_age)

    print()

    # set initial value 
    game_score = 0
    game_score += 3
    game_score += 9
    print(f"final score is : {game_score}")

    print()

    # string initial value
    ip_address = ""
    ip_address = "188"
    ip_address += "0:495"
    ip_address += ":9485"
    print(ip_address)
    print(type(ip_address))
    print(type(34))

    return

def main():
    variable_concept()
    return
main()

'''
    output
    ------
    27
    5.6
    theprakash97
    M
    False

    30
    60
    final score is : 12
    1880:495:9485
    <class 'str'>
    <class 'int'>

'''