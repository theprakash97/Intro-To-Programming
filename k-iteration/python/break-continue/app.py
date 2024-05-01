

def main():

    numbers = list(range(0,9))
    print(numbers)

    # break
    for x in numbers:
        if (x == 5):
            break
        print(x)

    print()

    # continue
    for x in numbers:
        if (x == 5):
            continue
        print(x,end=" ")


    return

main()