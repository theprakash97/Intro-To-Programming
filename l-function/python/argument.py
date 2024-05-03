
'''
    Arguments are often confused with parameters, and the main difference between both is that a parameter is a variable inside the parenthesis of function, while the argument is a actual_value passed to it.

    Type of pyhton function arguments : 
     - Default Arguments
     - Keyword Argument
     - Positional Argument  
     - Arbitary Arguments
     - Required Arguments

    // Default Arguments 
     A parameter can a have default, can be omitted in the function call. The function will then use the default value. In pyhton, function can have some default argument values that we provide to the function at the time of function declaration. 

     Some rules regarding default arguments are : 
   - There can be any number of default arguments in a function.
   - Whenever we declare a function, the non-default arguments are specified 
     before the default arguments. The default arguments are specified at the end, meaning any arguments specified to the right of a default argument must also be a default one. It is to prevent any ambiguity by the pyhton interpreter.

    // Keyword Arguments
    The term “keyword” is pretty self-explanatory. It can be broken down into two parts— a key and a word (i.e., a value) associated with that key.

    The parameter_name identifies these and can be supplied in any order, making your code more readable. For instance, func(a=1, b=2) explicitly states which parameter each argument corresponds to.

    Another advantage of using keyword arguments over positional arguments is that it makes the code more human-readable and understandable, which is essential if you are working with a team of developers on a single code base.

    // Positional Arguments
    Positional arguments are called according to their position in the function definition. The first argument in the call corresponds to the first parameter in the function's definition, the second to the second parameter, and so on.

    // Variable-length Arguments 
    Variable length arguments, also known as Arbitrary arguments, play an essential role in Python. Sometimes, at the time of function declaration, the programmer might need to be more specific about the number of arguments to be passed to the function to run it. Another way to put it is that the number of arguments might vary each time the function is called. In these cases, we use arbitrary arguments in Python.

    There are 2 ways to pass variable-length arguments to a python function : 
     - Arbitrary positional arguments (*args)
     - Arbitrary keyword arguments (**kargs)

    Arbitrary Positional Arguments (*args)
    ---------------------------------------
    The first method is by using the single-asterisk (*) symbol. The single asterisk is used to pass a variable number of non-keyworded arguments to the function. At the time of function declaration, if we use a single-asterisk parameter (e.g., *names), all the non-keyword arguments passed during the function call are collected into a single tuple before being passed to the function.

    Arbitrary Keyword Arguments (**kargs)
    ---------------------------------------
    You can also pass several keyworded arguments to a Python function. For that, we use the double-asterisk (**) operator. At the time of function declaration, using a double-asterisk parameter (e.g., **address) results in collecting all the keyword arguments in Python, passed to the function at the time of function call into a single Python dictionary before being passed to the function as input.


'''

# Default Arguments
def add_two(a,b=4):
    sum = a + b
    print(sum)
add_two(3) # 7 

# Keyword Arguments
def divide_two(a,b):
    res = a / b
    return res

res1 = divide_two(a=3,b=12) 
print(res1) # 0.25
res2 = divide_two(36,b=12)
print(res2) # 3.0
res3 = divide_two(b=12, a=48)
print(res3) # 4.0

# Positional Arguments
def add(a,b):
    return a + b
result = add(2,3)
print(result) # 5

# Arbitrary Positional Arguments (*args)
def print_animals(*animals):
    for animal in animals:
        print(animal,end=" ")
    print()

print("Lion","Elephant","Wolf","Zebra","Gorilla")

# Arbitrary Keyword Arguments (**kwargs)
def print_food(**foods):
    for food in foods.items():
        print(food)
print_food(Lion="Non-veg",Elephant="Veg",Gorilla="Veg")
print()
# The function can also have a combination of arbitrary keyword and non-keyword arguments, as shown in the example below : 
def print_animal_details(*animals,**foods):
    for animal in animals:
        print(animal)
    for food in foods.items():
        print(food)
print_animal_details("Lion","Elephant","Wolf","Gorilla",Lion='Non-veg',Elephant="veg",Gorilla="veg")
'''
In the example shown above, we can see that all the non-keyworded function arguments (i.e., “Lion”, “Elephant”, “Wolf”, and “Gorilla”) were collected and stored in the tuple animals. On the other hand, all the keyworded arguments were collected in the dictionary foods.

'''

'''
    Important Points to Remember about Function Argument :

    // Necessity of Positional Arguments Before Default Arguments : 
    In Python, arguments with default values (default arguments) must be defined after all the positional arguments without default values. This ensures the interpreter correctly assigns values to arguments when the function is called. 

    // Positional Arguments Precede Keyword Arguments :
    When calling a function, arguments without a keyword (positional arguments) should come before those specified with keywords. This rule helps the Python interpreter understand which values correspond to which parameters.

    // Flexibility in Ordering Keyword Arguments : 
    While the sequence of keyword arguments in a function call doesn't matter, each keyword argument must correspond to a parameter defined in the function. This allows more readability and flexibility in function calls.

    // Unique Assignment for Each Argument : 
    When calling a function, ensure that no argument receives a value more than once. Python will raise an error if a parameter is given multiple values in a function call.


'''

print()

# Necessity of Positional Arguments Before Default Arguments
def greet(name,message="Hello"):
    print(f"{message}, {name}")
greet("Prakash")
greet("Piyali","Good morning")

# Positional Arguments Precede Keyword Arguments
def print_info(name,age):
    print(f"Name : {name}, Age : {age}")
print_info("Caroline",age=32)

# Flexibility in Ordering Keyword Arguments
def set_profile(name,age,country):
    print(f"Name : {name}, Age : {age}, Country : {country}")
set_profile(age=25,country="USA",name="Jack")

# Unique Assignment for Each Argument
def display_values(a,b):
    print(f"a : {a}, b : {b}")
display_values(1, b=2) # correct
# display_values(1, a=3) # incorrect, raises an error 

















