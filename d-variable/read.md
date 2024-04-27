
# index 
> - Intro to variable 
> - Statically typed Vs Dynamically typed 
> - Syntax of variable 
> - Declaration Vs Initialization
> - Strongly Vs Weakly typed 
> - How to check data types of variable
> - Case_sensitive 
> - Naming rules of variables 
> - Scope 
> - Constant variables 
> - Statements and Expression forms of variables 
> - Reference_variable Vs Normal_variable
> - Primitive_variable Vs Reference_variable
> - Stack Vs Heap

## Intro To Variable 
Variables are named of the memory location to store data, which may get modified 
throughout the program execution . 

| Language | Variable Information |
| --- | --- |
| c++ | c++ is a strongly statically typed language , which means we must have to specify the type for variable declaration , function declaration & return type and variable expressions evaluation and  there is no binding which means we can’t use variables before they are declared . `int userAge;`  // declare statement  | 
| python | Python has no command for declaring a variable. A variable is created the moment assigned a value to it.<br><br>Python is a dynamically and strongly typed programming language :-- <br> **dynamically** : it means, there is no need to explicitly define the type of variable declaration,the interpreter automatically figure-out the type based on the assigned value of the variable at runtime. <br> **strongly** : strongly typed languages, the data type of variable is enforced at compile time, this means that the compiler checks the type compatibility and raises an error if there is a type mismatch.strongly typed language provides more safety and prevents common programming errors related to type casting/conversion.<br><br>Syntax : `variable_name  = object` <br><br>In python, everything is an object, when we store any information/data in a variable it becomes an object . An object is  any real-world entity that contains data along with properties and methods . In python, memory is allocated for an object not for a variable and an object is created only once in python, multiple variables can reference that object.<br><br>Each object consists of 3 field : <br> - type <br> - value <br> - reference_count.<br><br>A variable is just a label/reference to an object .|
| javascript | JavaScript is also a typed-inferred language , so we don’t have to explicitly define the type for variable declarations , function declarations & return type  and expressions evaluation  , the JavaScript  interpreter automatically figure-out the type during the runtime , based on the value .<br>In order to create variable in JavaScript we can use either ( var , let , const ) and followed by the varibaleName and semicolon ( ; ). <br>`var  userAge ;` //  declare statement |

## Statically Vs Dynamically Typed 

| Language | Descriptions |
| ---      | ---          |
| Statically | → Type checking is completed at compile time<br>→ Explicitly define the type declaration<br>→ Errors are detected earlier<br>→ Variable assignments are static & can’t be changed<br>→ Produce more optimized code<br>→ Slower development cycle<br>→ Type checking occurs at compile time |
| Dynamically | → Type checking is completed at runtime<br>→ No need to explicitly specify the type declaration<br> → errors are detected later during execution<br>→ variable assignment are dynamic and can be changed<br>→ Produce less optimized code<br>→ Faster development cycle<br>→ Type checking occurs at runtime . 

## Syntax Of Variable 

| Language | Syntax |
| ---      | ---    |
| c++ | data_type varibale_name = value ; |
| python | variballe_name = object ; |
| javascript | variable-keyword varibale_name = value ; |

## Declaration Vs Initialization 

| Declaration | the process of creation of variables is known as declaration |
| --- | --- |
| Initialization | the process of assigning the value to a variable is known as initialization | 

## Strongly Vs Weakly Typed

| Strongly | In a strongly typed language, the data type of a variable is enforced at compile-time. This means that the compiler checks for type compatibility and raises an error if there's a type mismatch.Strongly typed languages provide more safety and prevent many common programming errors related to data type mismatches.|
| --- | --- |
| Weakly | In a weakly typed language, the data type of a variable can be changed implicitly during runtime. Type conversions may happen automatically without explicit instructions from the programmer. Weakly typed languages offer more flexibility but can lead to unexpected behavior and errors if type conversions are not handled carefully.| 

## How to check data types of variable

| Language | Syntax |
| --- | --- |
| c++ | typeid(_varibale_name).name( ); |
| python | type( )<br>isinstance( ) |
| javascript | typeof | 

## Case Sensitive

Almost all programming languages care case-sensitive for variable names : 

> age  = 19 <br>
> Age  = 27 

In the above code snippet bothe `age` & `Age` are different variables .

## Naming Rules Of Variables

All variables must be identified with unique names . These unique names are called identifiers . 

Identifiers can be short names ( x and y ) or more descriptive names ( age, sum, totalVolume ) . It is recommended to use descriptive names in order to create understandable and maintainable code . 

// good<br>
`const  minutesPerHour = 60 ;`

// ok, but not so easy to understand<br>
`const m = 60 ;` 

> The general rules for naming variables are : 
>
> - Names can contains letters, digits and underscore 
> - Names must begin with a letter or an underscore ( _ ) 
> - Names are case-sensitive ( myVar and MYVAR ) are different variables
> - Names cannot contain whitespaces or special characters like !, #, %, etc , except  underscore(_) . 
> - Reserved keywords can’t be used as identifiers names . 

Variable names with more than one word can be difficult to read. There are several techniques we can use to make them more readable :

`Camel case` : Each word, except the first, strats with a capital letter :<br>
firstName = ‘John’<br>
`Pascal case` : Each word starts with a capital letter :<br>
FirstName = ‘John’<br>
`Snake case` : Each word is separated by an underscore character :<br>
first_name = ‘John’

## Scope

The scope determines the accessibility ( visibility ) of variables.<br><br>
There are 2 types of scope : <br>
1) Global scope
2) Block scope 

`Global variables`  : variables which are declared outside of blocks ( functions , classes , control-flow statements  ) are known as global variables . Global variables can be accessed from anywhere in programs.

`Local variables`  : variables which are declared inside a block ( functions, classes , control-flow statements ) are known as local variables. Local variables can be accessed inside the block only, can’t be accessed outside of the block. Local variables are created when the block starts execution and deleted when the execution of blocks is completed .  

## Constant Variables

| Languge | Descriptions |
| --- | --- |
| c++ | The `const` keyword is used to create a constant variable (which means unchangeable and read-only)|
| python | A CONSTANT is a special type of variable whose value cannot be changed throughout the execution of the program.<br><br>In python , the constants are usually declared and assigned in a module ( a new file containing variables , functions etc , which is imported to the main file ).<br><br>`NOTE` : In reality , we don't use constants in python. Naming constant variables in all capital letters is good convention to separate them from variables . However , it doesn't prevent reassignment. |
| javascript | Constant variable is a variable that value should not be changed through-out the program execution.<br><br>Some programming languages provide a keyword to create a constant variable in a program :-<br>For example : In `Java` has ‘final’ and `JavaScript` has a ‘const’<br><br>Here are some key characteristics of constant variables :- <br> - The value of constant variables shouldn't be changed.<br> - The constant variable must be declared and assigned, in the same line.<br><br>for examples :- <br><br>const PI = 3.14 ;<br>const minutesPerHour = 60;<br>const BIRTH_YEAR = 1980 ;<br><br>It is considered good practice to declare constant variables with an uppercase which differentiate from normal variables. | 


## Statements and Expression forms of variables

variable may included as part of statements and expression forms 

**statements :**  A line of code that instructs the compiler/interpreter to perform a specific task . statements  are usually composed of literal_value , variable , reserved_keyword , operator , or symbols . 

> let txt = ‘ hy ‘ ;<br>
> let res = txt + ‘ are you coming tonight ‘ + ‘  ? ‘ ;<br>
>console.log(res) ; // hy are you coming tonight ? <br>

**expression :** An expression is a combination of values, variables, and operators, which computes to a value . The computation is called an evaluation . 

> let principal = 85000 ; 
> let time = 2.5 ; 
> let rate = 7 
> let simpleInterest = ( principal * rate * time ) / 100 ; 

## Reference_variable Vs Normal_variable

Reference variables do not store their own values, rather they store address of another variable, while normal_variables typically directly contain their own_data . 

**reference_variables :** typically stores an object ( Array , Object , Map , Set , Stack , Queue , Linked list , )

**normal_variables :** typically stores the primitive_values ( data of primary data types ) 

A reference_variable is a variable that points to the address of another variable . It represents the name, location , or value of another variable .  

## Primitive_variable Vs Reference_variable

| Variable | Description | 
| --- | --- |
| Primittive variable |→ Primitive variables store values in stack memory.<br>→ Primitive variables are more memory-efficient and faster to access.<br>→ Primitive variables store only single data.<br>|
| Reference variable | → Reference variables store the address of an object.<br>→ Reference variables are more flexible.<br> → Reference variables store collection of multiple data.|

## Stack Vs Heap

Where is the program stored and executed in computers ? 
So, whenever we save our program into a file ( any kind of file , say ‘ server.py ‘ ) , it automatically gets stored in the secondary storage that is the Hard Disk .The operating system’s kernel ( kernel is a file management system )  does that .

When we run a program , it is loaded into the main / primary memory of the computer called RAM , the entire program is transferred to the RAM .
 
| Stack | Heap |
| --- | --- |
| A stack is a special area of computer memory which stores temporary variables created by a function . In stack , variables are declared , stored and initialized during runtime.<br><br>It is a temporary storage memory . when the computing task is complete , the memory of the variable will be automatically erased. The stack section mostly contains methods , local variables , and reference variables.| The heap is a memory used by programming languages to store an object & have referenced from the variable of stack memory.| 
| The stack is a data structure that follows LIFO ( Last in First Out ) principle .| The heap is a dynamically allocated memory space at runtime.|
| When a function is called, its local variables are pushed onto the stack . When a function returns, its local variables are popped off the stack. | Objects are stored in the heap. |
| The stack is used to store primitive data types , such as : string , number , boolean , bigint , symbol , undefined , null. | The heap is managed by the garbage collector, which automatically allocates and deallocates unused memory.<br><br>The Heap is used to store complex data structures, such as : Array , Objects , Functions . |
| Stores primitive data types and reference_variableNmaes of an object | Stores objects |
| Size is known at compile time | Size is known at runtime. |
| Fixed memory allocated | Not limit for object memory |






















