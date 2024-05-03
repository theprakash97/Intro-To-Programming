'''
    Functions are sub-program i'e part of the program that carries out some well defiend task. 

    Function are broadly didivded into 2 types : 
    1) Built-in functions/Library functions
    2) User-defiend functions 

    Function are brodly divided into 2 types : 
        1) Built-in function
        2) User-defiend function 

    Built-in function :--
    These are predefined functions, well optimized and tested functions that are readily available for use. for examples : len(), range(), and abs() . 

    User-defiend function :--
    These functions are created by users to perform specific tasks.

    // Function Declaration 
    In python, a function is declared using the 'def' keyword, followd by the function_name and parentheses and colon.


    Syntax : 
    def function_name(para1,para2,...paraN):
        # function body
    
    // Calling a function 
    A function is called by using its name followed by parentheses.In case parameters are present, these are include in the parenthese. for example : 

    def hello(txt):
        print(f"Hello {txt}")
    hello("Prakash")

    // function parameters
    Information can be passed to the function as a parameter . Parameters act as local variables inside the function. Parameters are specified after the function_name, inside the parentheses. We can add as many parameters as we want, just separate them with a comma. 

    Parameters are also known as formal parameters. Formal parameters are defined in the header of the function. The formal parameters are the variables defined in the header of the function that receives values when the function is called . 

    // function arguments 
    Arguments are the real value , if the parameter is present in the function definition, we need to pass the corresponding data value to the formal parameter of the function definition during the function call. The data we passed during the function is called arguments also known as actual parameters. 

    The Actual parameters are the values that are passed to the function when it is invoked. 

    Types of function arguments :--

    Pyhton support several types of arguments : 
    
    Positional Arguments
    -------------------------
    These are the most common arguments, where the argument's value is based on its position. For example, in func(a, b), a and b are positional arguments.

    Keyword Arguments
    --------------------------
    The parameter name identifies these and can be supplied in any order, making your code more readable. For instance, func(a=1, b=2) explicitly states which parameter each argument corresponds to.

    Default Arguments
    ---------------------------
    A parameter can a have default, can be omitted in the function call. The function will then use the default value.

    Variable-length Arguments
    ---------------------------
    You may need to determine the number of arguments supplied to your function. Python allows you to handle this with variable-length arguments, defined with an asterisk *args and **kwargs.


    for example : 
    
    def make_greeting(title, name, greeting="Hello"):
    return f"{greeting}, {title} {name}!"

    # Positional Arguments
    print(make_greeting("Dr", "Smith"))

    # Keyword Arguments
    print(make_greeting(name="Alice", title="Prof"))

    # Default Argument
    print(make_greeting("Mr", "Brown"))

    # All combined
    print(make_greeting("Ms", name="Johnson", greeting="Hi"))

    # output
    Hello, Dr Smith!
    Hello, Prof Alice!
    Hello, Mr Brown!
    Hi, Ms Johnson!

    // Docstring 
    In python, documentation strings, or docstrings, are literal strings used to document a python module, function , class, or method. They are essential for understanding and maintaing code, as they provide a convenient way of assciating documentation with python code.

    def add(a,b):
        """Add two number and return the result"""
        return a + b
    print(add.__doc__)

    # output
    Add two numbers and return the result

    // Nested functions 
    Function can be defined inside other functions. These nested functions help organize code into more manageable pieces, encapsulating functionality or creating closures adn decorators. for examples : 

    def outer_function(text):
        def inner_function():
            return text.upper()
        return inner_function()

    result = outer_function("hello")
    print(result)

    output
    ---------
    HELLO

    // Anonymous function 
    An anonymous in Python is a function that is defined without a name. Unlike functions defined using the def keyword, these are defined using the lambda keyword and are hence called lambda functions. They can have 0 or more arguments but only one return value.

    Syntax : lambda arguments: expression

    for examples : 
    
    square = lambda x: x * x
    print(square(2))

    The above example as a usually defined function could be written as:

    def square(x):
        return x * 2
    print(square(2))

    # output
    4

    // Recursive function
    Recursive is the process in which a function calls itself. Recursive functions and used mostly for sequence geenration and to make the code look clean and elegant. 

    // Library function
    Library function are predifined functions available in python libraries. These functions offer many functionalities without manual implementation, enhancing productivity and code efficiency. 

    import math
    result = math.sqrt(9)
    print(result)

    # output
    3.0

    // Return statement 
    The `return` statement exits a function and returns to the place where it was called. This statement can optionally return a value from the function to the caller. If no expression is specified, `None` is returned.

    Syntax : return [expressions]

    For example : 

    def add(a,b):
        return a + b
    result = add(5,3)
    print(result)

    # output
    8

    // Pass by Reference and Pass by Value 
    
    pass by reference 
    -----------------
    concept : a reference(or pointer) to the actual data is passed in passed_by_reference. Modifications to the parameter within the function affect the passed argument.

    python's approach : python deson't strictly follow this but behaves similarly with mutable objects. when a mutable object is passed, changes to it inside the function are reflected outisde the function.

    pass by value
    ------------------
    concept : pass by vaue means the actual value is passed. The function works on a copy, and changes within the function do not reflect the original data.

    python's approach : with immutable objects (like integers and strings), python's behavior is to pass_by_value. changes made to an immutable object in a function do not reflect in the original object.

    For example : 

    def modify_elements(collection):
        if isinstance(collection,list):
            collection.append(100) # this will affect
        else:
            collection += 10 # this won't affect
    
    # mutable 
    my_list = [1, 2, 3]
    modify_elements(my_list)
    print(my_list)

    # immutable 
    my_num = 7
    modify_elements(my_num)
    print(my_num)

    output
    --------
    [1,2,3,100]
    7

    // Benefit of function
    
    Modularity : Functions allow you to break down a complex problem into smaller, more manageable pieces. Each function can address a specific task or subproblem.

    Reusability : Once you've defined a function, you can use it multiple times throughout your code. This reduces redundancy and makes it easier to maintain and update code.

    Readability : Functions make code more readable and understandable. Well-named functions provide a clear indication of what a specific part of the code is 
    supposed to do.

    Abstraction :  Functions allow you to abstract away the implementation details of a particular task. The user of the function only needs to know what the function does, not how it achieves it.

    Testing and Debugging : Functions make it easier to test and debug code. Since each function performs a specific task, you can isolate issues and test each function independently.

    Scoping : Functions often have their own scope, which means variables defined inside a function are typically local to that function. This helps avoid naming conflicts with variables in other parts of the program .
    


'''

def main():
    return 
print(main())