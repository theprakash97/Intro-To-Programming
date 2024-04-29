
def main():

    sym = 'g'
    print(sym)

    # character_value to ascii_value
    ch = 'g'
    print(f"The ascii value of {ch} is : {ord(ch)}")

    # ascii_value to character_value
    num = 103
    print(f"The character value of {num} is : {chr(num)}")

    # escape sequence character
    a = 'P'
    b = '\t'
    c = 'R'
    d = '\t'
    e = 'A'
    user_name = a + b + c + d + e + '\n' + f"my name start with (pra + kash)"
    print(user_name)

    return

main()

'''
    output
    -------
    g
    The ascii value of g is : 103
    The character value of 103 is : g
    P       R       A
    my name start with (pra + kash)
    
'''