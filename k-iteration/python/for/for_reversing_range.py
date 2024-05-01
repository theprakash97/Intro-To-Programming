'''
    Reversing a range using negative step value 
    Reversing a range using reversed() function

'''

def main():

    # reversing a range using negative step value
    for i in range(5,0,-1):
        print(i)
    
    print()

    # reversing a range using reversed() function
    for i in reversed(range(1,6,1)):
        print(i)

    return

main()
'''
    output
    --------
    5
    4
    3
    2
    1

    5
    4
    3
    2
    1
    
'''