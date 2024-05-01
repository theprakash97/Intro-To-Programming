
def while_with_else():

    n = 1

    # 'else' block execute when the condition is Ture
    while(n < 9):
        print(n)
        n = n + 1
    else:
        print("end here")

    print()

     # 'else' block also execute when the condition is False
    while(n > 9):
        print(n)
        n = n + 1
    else:
        print("end here..")

    print()

    # break
    # here 'else' block not execute
    i = 1
    while(i < 9):
        if i == 5:
            break
        print(i)
        i = i + 1
    else:
        print('over!')
    
    return

def main():
    while_with_else()
    return
main()