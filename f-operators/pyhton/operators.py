
def main():

    # Arithmetic operators 
    a = 4
    b = 9
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a ** 2)

    print()

    # Unary operators 
    a = 5
    print(+a)
    print(-a)
    a = a + 1
    print(a)
    a = a - 2
    print(a)

    print()

    # Relational operators 
    print(4 < 9)
    print(4 <= 9)
    print(4 > 9)
    print(4 >= 9)
    print(4 == 9)
    print(4 != 9)

    print()

    # Logical operators
    print(4 < 9 and 4 != 9)
    print(4 > 9 or 4 != 9)
    print(not(4 != 9))

    print()

    # Identity operators 
    x = 5
    y = x
    print(x is y) # True
    print(x is not y) # False

    print()

    # Membership operators 
    user_name = "theprakash97"
    print("sh" in user_name) # True
    print("shy" not in user_name) # True

    # Bitwise operators 

    return

main()

'''
    output
    ----------
    13
    -5
    36
    0.4444444444444444
    0
    16

    5
    -5
    6
    4

    True
    True
    False
    False
    False
    True

    True
    True
    False

    True
    False

    True
    True
    
'''