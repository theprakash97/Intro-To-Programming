
def main():

    list1 = [1,2,3]
    list2 = [4,5,6]
    # Nested while loop 
    i = 0
    j = 0
    while(i < len(list1)):
        j = 0
        while(j < len(list2)):
            print(list1[i],"->",list2[j])
            j += 1
        print()
        i += 1

    return

main()

'''
    output
    ------
    1 -> 4
    1 -> 5
    1 -> 6

    2 -> 4
    2 -> 5
    2 -> 6

    3 -> 4
    3 -> 5
    3 -> 6
    
'''