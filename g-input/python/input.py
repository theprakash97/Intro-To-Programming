
def take_user_input():
    user_firstname = input("enter your firstname : ")
    user_age = int(input("enter your age : "))

    if(user_firstname == "sofia" and user_age >= 18):
        print(f"Hello {user_firstname}!")
        print("Access to attend a party #tonight")
    else:
        print("sorry not have access")

    return

def main():
    take_user_input()
    return

main()

'''
    output
    ---------
    enter your firstname : Prakash
    enter your age : 27
    sorry not have access

    Hello sofia!
    Access to attend a party #tonight


'''