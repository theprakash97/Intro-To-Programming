
def main():

    '''
  - Iterating over a dictionary 
  - Accessing values of a dictionary 
  - Acessing keys of a dictionary
  - Acessing keys and values of a dictionary
    '''

    # for loop can be used to iterate over a dictionary : =>
    course = {
        "name" : "Python",
        "instructor" : "Andrew Tate"
    }

    for x in course:
        print(x)

    print()


    # Accessing values of a dictionary : => 
    
    # values can be accessed using square-bracket notation 
    for x in course:
        print(course[x])

    # values can also be accessed using values() method 
    for v in course.values():
        print(v,end="->")
    print('\n')

    

    # Accessing keys of a dictionary : =>
    # keys can be accessed using keys() method 
    for y in course.keys():
        print(y)
    
    print()
    

    # Acessing keys and values of a dictionary : => 
    # keys and values can be accessed by using items() method 
    for x,y in course.items():
        print(x,'->',y)
    


    return

main()