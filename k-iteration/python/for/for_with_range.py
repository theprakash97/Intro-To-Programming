
'''

    Introduction to the range() function 
    for loop with range(stop)
    for loop with range(start,stop)
    for loop with range(start,stop,step)


    points :  
  - The range() function only works with integer arguments.
  - All three arguments can be positive or negative.
  - The step value cannot be zero

'''

def main():

    # introduction to the range() function 
    # sytnax : range(start,stop,step)

    # for loop with range(stop)
    for i in range(5):
        print(i)
    
    print()

    # for loop with range(start,stop)
    for i in range(3,9):
        print(i)
    
    print()

    # for loop with range(start,stop,step)
    for i in range(1,13,2):
        print(i)
    

    return

main()