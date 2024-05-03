
'''
    Scope
    -------
    The scope determines the accessibility ( visibility ) of variables . 
    
    There are 2 types of scope : 
    - Global scope 
    - Block scope 

    // Global variables  :
    variables which are declared outside of blocks (functions ,classes , control-flow statements  ) are known as global variables . Global variables can be accessed from anywhere in programs.

    // Local variables  : 
    variables which are declared inside a block ( functions, classes , control-flow statements ) are known as local variables. Local variables can be accessed inside the block only, can't be accessed outside of the block. Local variables are created when the block starts execution and deleted when the execution of blocks is completed .  


'''

# Local variable
def calculate_area(r):
    PI = 3.1415
    area = PI * r * r
    print(f"The area of the cirlce is : {area}")

calculate_area(5)
# print(PI) # can't access PI

# Global variable
z = 50
def fun():
    print(z) # 'z' is accessible here 
fun()
print(z) # 'z' is accessible here

'''
    Nonlocal variables
    ------------------------
    In python, the `non-local` keyword, like 'global', declares a variable. However, `nonlocal` specifically references a variable in an outer enclosing function within a nested function.

    The `nonlocal` keyword allows modifying variables from the outer enclosing function within a nested function.
'''

print("Value of string_var using nonlocal is : ",end=" ")
def outer_func_one():
    string_var = "Hello"
    def inner_func():
        nonlocal string_var
        string_var = "world"
    inner_func()
    print(string_var)

outer_func_one()
# output
# Value of string_var using nonlocal is :  world

print("Value of string_var without using nonlocal is : ",end=" ")
def outer_func_two():
    string_var = "Hello"
    def inner_func():
        string_var = "world"
    inner_func()
    print(string_var)

outer_func_two()
# output
# Value of string_var without using nonlocal is :  Hello

