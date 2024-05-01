
def main():

    '''
   - Iterating over a list 
   - Iterating over a list using for loop and range()
   - list comprehension

    '''

    # Iterating over a list 
    cars = ["audi","bmw","toyota"]
    for car in cars:
        print(car)
    
    print()
    
    # Iterating over a list using for loop and range()
    for item in range(len(cars)):
        print(cars[item],end= " ")
    
    print('\n')

    # List comprehension
    # List compreshension can produce the result in less lines of code
    [print(item) for item in cars]
    


    return

main()