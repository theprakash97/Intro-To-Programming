
def main():
    '''

    - Accessing characters of a string 
    - Iterating a string in reverse order 
    - Accessing words of a string 

    '''

    # Accessing characters of a string : for loop can be used to access all   characters of string

    user_name = "theprakash97"
    for cvl in user_name:
        print(cvl,end=" ")
    print()

    print()

    # Iterating a string in reverse order 
    user_name = "sofia_kal"
    for cvl in user_name[::-1]:
        print(cvl,end=" ")
    print()

    # Accessing words of a string
    user_location = "gopalpur sea beach"
    count = 0
    for word in user_location.split():
        count += 1
    print(f"There {count} words in 'user_location'")
    


    return

main()