
def type_casting():

    # <<< implicit type conversion >>>
    a = 7
    b = 3.0

    # Python automatically converts `c` to float as it is a float addition
    c = a + b
    print(c,type(c))

    print()

    # <<< explicit type conversion >>>

    # int → float 
    x = 5
    res = float(x) ; print(res,type)

    # float → int
    p = 79.98753
    res = int(p); print(res,type(res))

    # int → string 
    num = 79
    res = str(num); print(res,type(res))

    # str → float 
    numeric_txt = "5.9"
    res = float(numeric_txt); print(res,type(res))

    # str → int 
    # res = int(numeric_txt); print(res,type(res)) # ValueError: invalid literal for int() with base 10: '5.9'
    # if the given string is not number, then it will throw an error

    return

def main():
    type_casting()
    return

main()

'''
    output
    --------
    10.0 <class 'float'>

    5.0 <class 'type'>
    79 <class 'int'>
    79 <class 'str'>
    5.9 <class 'float'>

'''