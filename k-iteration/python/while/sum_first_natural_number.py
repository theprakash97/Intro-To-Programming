
def sum_first_natural_number():
    n = int(input("enter a number : "))
    copy_vl = n
    sum = 0
    while n > 0:
        sum += n
        n = n - 1
    print(f"sum of first natural number of {copy_vl} is : {sum}")
    return

def main():
    sum_first_natural_number()
    return
main()