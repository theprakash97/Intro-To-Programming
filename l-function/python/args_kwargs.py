
'''
    *args specifies the number of non-keyword arguments that can be passed and the operations that can be performed on the function in python, whereas **kwargs is a variable number of keyworded arguments that can be passed to a function that can perofrm dictionary operations.
'''

'''
    // Python *args
    -------------------------------------
    // Let us assume that you are building a calculator, which only performs multiplication.

    def multiply(num1,num2):
        return num1 * num2
    print("product :",multiply(2,3))

    // Now, you want to multiply three numbers, so you have to make 
    // a new function :

    def multiple_three_numbers(num1,num2,num3):
        return num1 * num2 * num3
    print("product :",mulitple_three_numbers(1,2,3))

    You can already see the problem. If you keep going on like this, you will end up doing a lot of functions.

    *args can save you the trouble here. You can use `*args` to solve this problem in a simple and flexible piece of code : 
    
    def multiply_numbers(*numbers):
        product = 1
        for n in numbers:
            product *= n
        return product
    print("product :",multiply_numbers(4,4,4,4,4,4))
    # output
    product:4096

    Python has *args, which allows us to pass a variable number of non-keyword arguments to a function. Non-keyword here means that the arguments should not be a dictionary (key-value pair), and they can be numbers or strings.

    One thing to note here is that "args" is just an identifier. It can be named anything relevant.

    When an asterisk(*) is passed before the variable name in a Python function, then it understands that here the number of arguments is not fixed. Python makes a tuple of these arguments with the name we use after the asterisk(*) and makes this variable available to us inside the function. This asterisk(*) is called an “unpacking operator”.
    This variable is then available to inside the function, and we can use it to perform any operation we want. In our case, we iterated (looped) over it and calculated the product of all the numbers.

'''

'''
    // Python **kwargs
    ---------------------------------------------
    *args enable us to pass the variable number of non-keyword arguments to functions, but we cannot use this to pass keyword arguments. Keyword arguments mean that they contain a key-value pair, like a python dictionary.

    **kwargs allows to pass any number of keyword arguments.In python, these keyword arguments are passed to the program as a python dictionary.

    Python will consider any variable name with two asterisks(**) before it as a keyword argument.
    def makeSentence(**words):
        sentence = ''
        for word in words.values():
            sentence += word
        return sentence
    print("sentence :", makeSentence(a='KWargs',b='ar ',c='awesome!'))
    # output
    Sentence: KWargs are awesome! 

    In the makeSentence function, we are iterating over a dictionary, so we have to use values() to use the values. Otherwise, it will only return the keys and not the values.

    Another example of how kwargs can be used is given below :
    def what_tech_they_use(**kwargs):
        result = []
        for key, value in kwargs.items():
            result.append("{} use {}".format(key,value))
        return result

    print(whatTechTheyUse(Google='Angular', Facebook='react', Microsoft='.NET'))
    
    # output
    [‘Google uses Angular’, ‘Facebook uses react’, ‘Microsoft uses .NET’]

    In this code, we have used .items() because we want to get both the key and the value.

'''

'''
    // Using both *args and **kwargs in python to call a function 
    -----------------------------------------------------------------
    Now that you have understood *args and **kwargs, you might want to design a function that uses both of them. While doing this, the order of the arguments matters; *args have to come before **kwargs.

    So, if you are using standard arguments along with *args and **kwargs, then you have to follow this order :--
    1. Standard Arguments
    2. *args
    3. **kwargs

    A simple example of a function that uses standard arguments, *args and **kwargs in Python : 

    def printingData(codeName, *args, **kwargs):
    print("I am ", codeName)
    for arg in args:
        print("I am arg: ", arg)
    for keyWord in kwargs.items():
        print("I am kwarg: ", keyWord)
 
    printingData('007', 'agent', firstName='James', lastName='Bond') 

    # output
    I am 007 
    I am arg: agent 
    I am kwarg: (‘firstName’, ‘James’) 
    I am kwarg: (‘lastname’ , ‘Bond’)

'''