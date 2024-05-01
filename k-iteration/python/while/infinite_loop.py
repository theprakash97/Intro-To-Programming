
def infinite_loop():

    # loop can run infinitely if the condition never becomes `False`

    n = 100

    '''
    // infinite loop 
    while True:
        print(n)
        n = n - 1
    '''

    # break 
    while True:
        print(n)
        if n == 95:
            break
        n = n - 1

    return

def main():
    infinite_loop()
    return
main()