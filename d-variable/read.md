
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

## Strongly Vs Weakly typed















