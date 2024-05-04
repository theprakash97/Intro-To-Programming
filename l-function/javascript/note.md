
## Function

> - Intro to function 
> - Benefit of function
> - Types of function 
> - Declaration of functions 
> - Function Invoke
> - Return value
>    - single return
>    - multiple return
> - Pass_by_value Vs Pass_by_reference
> - Difference between function Vs method 
> - `this` keyword & function object
> - Scope 
> - Hoisting 
> - Closures
> - Type of functions in JavaScript 
> - High order function
> - Function are first class citizens in JavaScript 
> - Callback function 


## Intro  to function 

A function is a resuable block of code designed to perform a specific task or set of tasks. Functions help organize code, make it more modular, and allow us to reuse the same code in different parts of programs. 

Suppose we need to create a program to create a circle and color it , we can create two functions to solve this problem :

 -  A function to draw the circle 
 -  A function to color the circle 


Functions allow us to divide a complex problem into smaller chunks and makes our program easy to understand and reusable .

## Benefit of function 

`Modularity` : Functions allow you to break down a complex problem into smaller, more manageable pieces. Each function can address a specific task or subproblem.

`Reusability` : Once you've defined a function, you can use it multiple times throughout your code. This reduces redundancy and makes it easier to maintain and update code.

`Readability` : Functions make code more readable and understandable. Well-named functions provide a clear indication of what a specific part of the code is supposed to do.

`Abstraction` :  Functions allow you to abstract away the implementation details of a particular task. The user of the function only needs to know what the function does, not how it achieves it.

`Testing and Debugging` : Functions make it easier to test and debug code. Since each function performs a specific task, you can isolate issues and test each function independently.

`Scoping` : Functions often have their own scope, which means variables defined inside a function are typically local to that function. This helps avoid naming conflicts with variables in other parts of the program . 


## Types of function

`Built-in Functions` : Programming languages come with a set of built-in functions that perform common tasks. Examples include print() in Python, which outputs text to the console, or Math.abs() in JavaScript, which returns the absolute value of a number.

`User-Defined Functions` : These are functions created by the programmer to perform specific tasks. User-defined functions enhance code modularity and reusability.

`Recursive Functions` : A recursive function is one that calls itself during its execution. This can be a powerful technique for solving problems that can be broken down into smaller, similar subproblems.

`Anonymous Functions (Lambda Functions)` : These are functions without a name. They are often used for short, one-time tasks. In languages like Python, you can create anonymous functions using the lambda keyword.

`Higher-Order Functions` : These are functions that can take other functions as arguments or return functions as results. They enable a more functional programming style.

`Pure Functions` : Pure functions have two main characteristics: they always produce the same output for the same input, and they have no side effects. This makes them predictable and easier to reason about.

## Declare function

One of the ways to define a function is a function declaration. When you create a function with a name, it’s called a function declaration (aka function definition or function statement) .

This is the most standard, basic way of writing a function and what you will use very often as a beginner.

> function sendMessage( sms ) {<br>
>     console.log(sms) ;<br>
>     return;<br>
> }

The function declaration consist of  : 

>A `function` keyword.<br>
>The name of the function with respecting identifiers rules.<br>
>A parenthesis that holds the parameters.<br>
>The body of the function, enclosed within a pair of curly braces . This is the place where we can provide function instructions.<br>
>`return` is a reserved keyword, it denotes the function execution is complete. Any code after the return statement will not be executed , often referred to as a dead_codes. 

## Function Invoke

Function is executed , when it is invoked ( call function / start the function ) 

Function must be invoked followed by parentheses ( ).

Functions are executed in the sequence they are called. Not in the sequence they are defined.

>function greet(){ // function defination or function signature <br>
>    // body of the function<br>
>}<br>
greet() // calling function 

If we just define a function , then it is of no use until we actually call it .
To call a function , simply write the functionName followed by the parentheses .

Important points when calling the functions  : 
> - All arguments in JavaScript functions are optional or loosely typed .
> - JavaScript function can be invoked with any number of arguments .
> - Since a function is loosely typed, we can pass any number of arguments to it .
> - When a function is invoked with fewer arguments than that are declared , the additional arguments have the default value → undefined .

Functions are only executed when it is invoked, NOT when it is defined. 

## Parameters & Arguments 

`Parameters` : Information can be passed to the method as a parameter . Parameters act as local variables inside the method . Parameters are specified after the method name, inside the parentheses . We can add as many parameters as we want , just separate them with a comma . 

Parameters are also known as formal parameters . Formal parameters are defined in the header of the function . The formal parameters are the variables defined in the header of the method that receives values when the function is called . 

`Arguments` : Arguments are the real value , if the parameter is present in the method definition , we need to pass the corresponding data value to the formal parameter of the method definition during the method call . The data we passed during the method is called arguments also known as actual parameters . 

The Actual parameters are the values that are passed to the function when it is invoked . 

What are the similarities between Formal and Actual parameters :--
> - Both are related to functions .
> - Parameters are included inside the parentheses . 
> - Each parameter is separated by a comma . 

| Formal parameters | Actual parameters | 
| --- | --- |
| The Formal parameters are the variables defined in the header of the method that receives values when the method is called. | The actual parameters are the values that are passed to the method when it is invoked/called. |
| In formal parameters , the data types of the receiving values must be included. | In actual parameters , there is no mention of data types . Only the value is mentioned. |

---

for example : 

>function greet(name,age){<br>
>    var x = `Hello {name} i am ${age} year old;<br>
>    return x;<br>
>}<br>
>greet("Sofia",29);<br>

When values are passed after declaring a function, it is called parameter, And when the functions are called , the values passed are called arguments.

The arguments are the real values , it will be passed to the parameter of the function definition when the function is invoked ( call function ) .

Inside the function, the parameters behave as local variables.
And the function can have any number of parameters and arguments and can be empty also.

### Rest paremeter/operator Vs Spread operator 

`Rest operator` : When the spread operator is used as a parameter, it is known as the rest parameter or rest operator. 

We can pass multiple parameters into a method . But what if we don’t know how many arguments we need to pass ? restParameter ( …restPara ) is a trick that accepts a variable number of arguments . 

Syntax : 

>function dataFromServer( para1, para2, ….., paraN, …restPara ) {<br>
>// function body<br>
>}<br>

There main thighs to note are : 
> - Rest parameter starts with three dots and follows the parameterName ( …restPara ) . 
> - Each function can have only one …restParameter . 
> - In the case of multiple parameters, the  …restParamter must be the last parameter in the function definition . 

Rest parameter allows us to represent any number of arguments ( indefinite ) as an array.

`Spread operator` : The spread operator(...) is used to expand or spread an iterable or an array . 

Using rest parameter will pass the arguments as array elements.

Syntax :<br>
> function name( x , y , z, …args ) { <br>
>      // body of function<br>
>} 

example :

> let  x = function ( …args ) {<br>
>      console.log(args) ;<br>
>}<br>
x(3); // [ 3 ]<br>
x( 4, 5, 6 )  // [ 4, 5, 6 ]

We can also pass multiple arguments to a function using the spread operator. For example,

> function  sum ( x , y , z ) {<br>
>  console.log ( x + y + z );<br>
}
>
>const num1 = [ 1 , 3, 4 , 5 ];<br>
>sum ( ...num1 ); // 8 

If you pass multiple arguments using the spread operator, the function takes the required arguments and ignores the rest.

### Rest parameter Vs Argument objects

`Rest parameter` : When the spread operator is used as a parameter, it is known as the rest parameter.
Basically the rest parameter is used, when we don’t know how many arguments will be received  to the function when the function is called , to handle this kind of stuff we use the rest parameter.<br><br>
`Command Line Arguments`  : The command-line argument is an argument that is supplied when the javaScript program is run . The arguments given from the terminal can be received and used as input in the javaScript program . 

NOTE : All the variables through the command line are considered as string , we will have to explicitly type-cast them to be used as integers or other data types . 

The arguments object behaves like an array , but it is not an array and it is not an instance of the Array type.

For example, we can use the square bracket [ ] to access the arguments: 
arguments[0] returns the first argument, arguments[1] returns the second one, and so on . Also, you can use the length property of the arguments object to determine the number of arguments .

Getting an arguments with arguments object :
> - JavaScript functions have a built-in object called the arguments object .
> - We may say the “ arguments “ is an Array-like object which can be used inside the function to access the arguments of the particular function .
> - The arguments object contains the values of the arguments ( as an array ) which we pass to the function .
> - We can pass any number of arguments to the function and inside the function , these arguments can be accessed by referring to the index number with the arguments object 

see the below examples : 

>function ok(fname, ...x){<br>
>console.log(fname);<br>
>console.log(...x);<br>
>console.log(arguments);<br>
>
>console.log(arguments[0]);<br>
>console.log(arguments[1]);<br>
>console.log(x[0]);<br>
>console.log(x[1]);<br>
>console.log(arguments.length);<br>
>console.log(x.length);<br>
>console.log([x].fill('Jack Rayan'));<br>
>
>}<br>
>ok('Sofia','Hydrabad',25,'Pune',true,4.5);
>
>// output<br>
>Sofia<br>
>Hydrabad 25 Pune true 4.5<br>
>[Arguments] {<br>
>'0': 'Sofia',<br>
>'1': 'Hydrabad',<br>
>'2': 25,<br>
>'3': 'Pune',<br>
>'4': true,<br>
>'5': 4.5<br>
>}<br>
>Sofia<br>
>Hydrabad<br>
>Hydrabad<br>
>25<br>
>6<br>
>5<br>
>[ 'Jack Rayan' ]<br>

### Default Parameter Values

Function parameters can also have a default value , the default value is set if no value or undefined is passed to them.

> function add(a = 0, b = 0) {<br>
> return a + b;<br>
> }<br>
>
> console.log(add(10, 5)); //Calling with both the arguments<br>
> console.log(add(10)); //Calling with 1 argument<br>
> console.log(add()); //Calling with 0 argument<br>
>
>// output<br>
>15<br>
>10<br>
>0

Once a default parameter value is used  in the function definition, all subsequent parameters to it must have a default value as well. 
It can also be stated that the default parameters are assigned from right to left. For example, the following function definition is invalid because the last parameter doesn’t contain any default value : 

> function sum( x = 4, y = 5, z ); 

## Return values

Function can also have a return statement .

The return statement can be used to return the value to the function call .

The return statement denotes that functions has ended , any code after the return is not executed .

If nothing is returned , the function returns undefined value by default .

Functions often compute a return value , the return value is returned back to the caller .When JavaScript reaches a return statement , the function will stop executing .

By default JavaScript function returns single value ,
To return multiple values from the function , we can pack the return values elements of an array or as properties of an object .

// Returning multiple values from a function using an array :

For example ;<br>

    function getNames( ) {
        // get names from the database or API
        let  firstName = ‘ John ‘ ;
        let lastName = ‘ Doe ‘ ;

        // return as an array
        return  [ firstName , lastName ] ;
    }

    let  names = getName ( ) ;
Because the ‘ names ‘ variable is an array. We can access its elements using the index number in the square bracket.
const  firstName = names[ 0 ] , 
            lastName = names [ 1 ] ;
In ES6 ,we can use the destructuring assignment syntax to unpack values from an array :
const  [ firstName , lastName ] = getNames ( ) ;

// Returning multiple values from a function using an object :

For example ;<br>
If we want to assign a name to each returned value to make it more readable and easier to maintain, we can use an object :<br>

    function getNames( ) {
            // get names from the database or API
            let  firstName = ‘ John ‘ ;
            let lastName = ‘ Doe ‘ ;

        // return object
        return  {
                fname : firstName ,
                lname : lastName
        } ;
    }

Since the names of the properties are the same as the variables, we can shorten it using the object literal syntax extensions in ES6 :<br>

    function getNames( ) {
            // get names from the database or API
            let  firstName = ‘ John ‘ ;
            let lastName = ‘ Doe ‘ ;

        // return 
        return  { firstName , lastName } ; 
    }

And we can get the return values as an object like this :<br>

    let  names = getNames ( ) ;
    let  firstName = names.firstName ;
    let  lastName = names.lastName ;

    Or we can use object destructuring syntax like this : 
    let  { firstName , lastName } = getNames ( ) ;


## Pass by values Vs Pass by reference 

In JavaScript primitive  data types are passed by a value ,  And the  Non-primitive data types are passed by a reference .

Primitive data types in JavaScript are :<br>

    String
    Number
    Boolean
    Undefined
    Null
    Bigint
    Symbol
Non-primitive data types in JavaScript are :<br>

    Array
    Object 
    
`Pass by value` →   In the pass by value ,  the copy value of the original variable passed as an argument while calling the function . Anything that changes the copied variable inside the function does not reflect the outside of the original value of the variable . 

`Pass by reference` →   In the case of  the pass by reference ,  we pass the address of the original variable as an argument while calling a particular function . Anything that changes the passed variable inside the function will reflect the outside of the original value of the variable . 

Different between pass by value & pass by reference : 

| pass by | description |
| --- | --- |
| value | - The copy of the actual value is passed in method<br>- Memory consumption is more in the pass by value<br> - The pass by value process provides more security |
| reference | - The memory address of the original value is sent in the pass by reference.<br> - Memory consumption is less in the case of pass by reference.<br> - The pass by reference is less secure as compared to the pass by value. |

---
<br>

`When to use pass by value` ?
As in pass by value in JavaScript, a new copy of the original variable is created and any changes made in the new variable are independent of the original variable so it is useful when we want to keep a track of the initial variable and don't want to lose its value.

`When to use pass by reference` ?
When we are passing arguments of large size it is better to use pass by reference in JavaScript as no separate copy is made in the called function so memory is not wasted, and hence the program is more efficient .

## Function Vs Method 
| Function | Method | 
| --- | --- | 
| Can have many parameters | The object is one of its parameter | 
| exists on its own | belong to a certain class | 
| function ( ) | Object.method ( ) | 
| Not associated with objects | Associated with objects | 

---

## `this` keyword & Function object 

The `this` is a reserved keyword that always refers to an object .  It has a different meaning depending on how it is being invoked or called/used . 

The `this` keyword refers to different objects depending in how it is used : 
In an object method, `this` refers to the object
Alone, `this` refers to the global object
In a function, `this` refers to the global object
In a function, in strict mode, `this` is undefined 
In an event, `this` refers to the HTML element that received the event. 
Methods like ; call( ), apply( ) , bind( ) can refer `this` to any object.

Notes : `this` is not a variable. It’s a keyword ,can’t change value of `this`

In method : `this` refers to the object 
Alone : `this` refers to the global object, which is ( [object Window] )
In strict mode : `this` refers to the global object.
In a function : `this` refers to the global object.
With  strict mode in a function : `this` refers to undefined . 
In event : `this` refers to the HTML element that received the event.
Methods like call( ) , apply( ) , bind( ) : use `this` can point to any object .

The precedence to determine which object `this` refers to; use the following precedence of order : <br>

    precedence object    description 
    ---------- ------    -----------------------------------------
    1          bind( )   Is `this` in a function benign called using bind( ) ? 
    2          apply( )
               call( )   Is `this` in a function called using apply( ) or call( ) ? 
    3          object_method    Is `this` in an object function (method)  ? 
    4          Global_scope Is `this` in a  function in the global scope ? 

The `this` keyword enables to a function in JavaScript to be reused in different contexts – It helps make it possible to point the function to a particular object and all of its properties when it is invoked .

However , simply using this in function or method won’t bind it to the object it is used in . Functions are bound to a particular context at call time , not when they are declared .

> We will need to know the **5 types** of function binding and how they work :

`What is bind` :  The bind to make connection / association between two or more programming objects or values items for the same scope of times and place .

for example in JavaScript : We can bind an object to a common function , so that the function gives different results when it is needed.

`1) window binding` →

The most basic function binding is the default or window binding. 

When a function is freely invoked, such as myFunc( ) , it will always look to the global object for its context. In browsers, the global object is the window, or [object Window]. This is the fall back binding for all functions, and is most often identifiable when a function is called without using dot notation, otherwise known as free function invocation.

`2) Implicit binding` →

One of the most common ways the binding of this is defined is through implicit binding, which is also known as object method binding or method invocation .
This is when a function is called as a method of an object using dot notation . 


    let getName = {
    fname : 'Sara',
    message(){
    console.log(`I am ${this.fname}`);
    }
    };

    getName.message();
    // output
    I am Sara

In the above example :
If the method is part of an object and is called as such, this will be bound to that object’s context. In this example,message( ) looks for the fname property within getName to define this.name 

`3) Explicit binding` →

Whereas implicit binding uses method invocation to attach this to a particular object , there is another way to attach this when functions are not stored as methods in an object — explicit binding. Explicit binding forces a function call to bind to a particular context object, by using either call, apply, or bind. These are predefined JavaScript methods — properties inherited by all functions through the Function.prototype 

To give a standalone function a particular context at call time, simply use one of these methods( apply , call , bind )  on the function, passing in the desired context object as the first argument. Of course, these three methods don’t do the exact same thing. Let’s look at the basic differences :

> **.call( )** →
>
>immediately invokes the function.<br>
>first parameter is the context object.<br>
>all other parameters are individually listed, separated by commas.<br>

> **.apply( )** →
>
>immediately invokes the function.<br>
>first parameter is the context object.<br>
>all other parameters can be passed in as a single array.<br>

> **.bind( )** →
>
>does not immediately invoke the function.<br>
>returns a new function that can be invoked later in the code, while maintaining the desired context binding — this is useful for passing functions into other functions, like setTimeout(), which will invoke it later and won’t necessarily bind the invoked function to the correct object without being coerced.<br>
>first parameter is the context object.<br>
>all other parameters are individually listed, like with call.

`4) new binding` →

The new operator is used before a function call will also bind a particular context object to that invocation. However, new is not used for any kind of function call, but for constructor function calls. When new is used, the function’s parameters will be used to instantiate or create a new object with its own context. 

So, with the use of new we know the context of this for that new object — it’s own. Functions called with new are named with title case, as opposed to the JavaScript naming convention, camel case.

`5) Lexical binding` →

In ES6 , we can use the arrow function for syntactical simplicity . However , the functions declared with the function keyword are not interchangeable with arrow functions , and the primary difference is the way they handle this , whereas regular functions have their own this , arrow function doesn’t have its own this , and the this keyword in arrow function always referring to the paranet scope / outer scope . “ the this value used in arrow functions it actually fetched lexically from the scope it sits inside “ 

The lexical binding can also refer to how this can also be bound by the type of function used. This can make for less code when you want a function to inherit this from the outer scope, or can cause problems when you’d like to pass a context into a function .

In JavaScript, almost everything is an object, Function is also an object, It has properties and methods : 

    Function.length → Returns the number of parameters of a function 
    Function.name → Returns the name of the given function 
    Function.apply( ) → Calls function with `this` value and array of arguments 
    Function.call( ) → Calls a function with a given `this` value and separate arguments 
    Function.bind( ) → Crates new function with given `this` value and arguments 
    Function.toString( ) → Returns source code of function as a string 

## Scope 

Scope determines the accessibility ( visibility  ) of variables . 

Before ES6 ( 2015 ) , javaScript had only two scope - Global scope and Function scope .
**ES6** Introduced two important new javaScript keywords : `let` and `const` . These two keywords provide a block scope in JavaScript.

Typesof scope in JavaScript : <br>
1) Global scope 
2) Local scope 
3) Lexical scope 



`Global scope` : <br>
The variables which are declared outside of any  function or any block are known as global variables. 

Global variables have global scope . 

Global variables can be accessed from anywhere in a JavaScript program.
Variables declared with var , let and const are quite similar when declared outside a block. They all have Global Scope : <br>

    var  x = 2 ;  // global scope
    let   x = 2 ; // global scope
    const x = 2 ; // global scope 

If we assign a value to a variable that has not been declared, it will automatically become a global variable.
this code example will declare a global variable carName , even if the value is assigned inside a function .

    // code here can use 'carName'
    function myFunction( ) {
       carName = ‘ Volvo ‘ ;
    }
    myFunction ( ) ;

// Global variables 

in javaScript , the global scope is the javaScript environment.<br>

`In HTML` , the global scope is the window object .
So, 
Global variables defined with ‘ var ‘ keyword , by default belong to the window object.
> var  carName = ‘ Volvo ‘ ;
// code here can use window.carName

Global variables defined with `let` and `const` ,  do not belong to the window object.

    let  carName  = ‘ Volvo ‘ ;
    // code here can’t use as window.carName
    const  carName = ‘ Volvo ‘ ;
    // code here can’t use as window.carName 

> Strict mode; In " Strict Mode " , undeclared variables are not automatically global.
Warning ; Do NOT create global variables unless you intend to.
>
> Your global variables (or functions) can overwrite window variables (or functions). Any function, including the window object, can overwrite your global variables and functions.

> Function Arguments ; 
Function arguments ( parameters ) behave as local variables inside the functions.<br><br>

`Local scope` : <br>
The variables which are declared inside the block ( {...} ) are known as local variables. Local variables have local scope , the scope is limited inside the pair of curly braces, and can't be accessed outside of the curly braces . 

Block scope : `let` and `const` are Block scoped .

Variables declared with let and const have block scope , but variables declared with var can’t have block scope .

Block is also known as compound statements .

`Block` → Block is defined by the curly braces ( { … } ) , and the blocks are mainly used to define multiple statements , and enclosed within curly braces .

`Block scope` → Block scope means that all the variables and functions we can access inside the block is known as block scope .


`NOTES` : Block scope also follows the lexical scope . Lexical scope is lexically present , when we say lexically block scope it means , one block inside the another block .

Look the below examples :


    const a = 45;

    function ok(){
    const a = 7;
    {
        // let a = 5.6; // suppose a is not present here
        console.log(a);
    }
    console.log(a);
    }
    ok();
    console.log(a);

    //output
    7
    7
    45

> So lexical scope works the same way inside the block also . 

`Lexical scope` :<br>
Lexical scope is also known as lexical environment .
The lexical scope is the local memory + the references to the lexical environment / lexical scope of the parent .
In other words → The nested group of functions , the inner function will have access to the variables and the other resources of their parent scope / outer scope. <br>

For examples :

    const a1 = 5;
    function baseFunction(){
    const b = 76.3;
    {
        const a2 = true;
        console.log(a1); // 5
        console.log(b); // 76.3
        console.log(a2); // true
    }
    function innerFunction(){
        let y = null;
        console.log(a1); // 5
        console.log(b); // 76.3
        // console.log(a2); // CAN'T ACCESS
        console.log(y); // null
    }

    console.log(a1); // 5
    console.log(b); // 76.3
    // console.log(a2); // CAN'T ACCESS
    // console.log(y);  // CAN'T ACCESS
    innerFunction();
    }
    baseFunction();
    console.log(a1);// 5

> An inner function can access the variables and other resources of its parent function , vice versa is not applicable . 

## Hoisting

Hoisting is a phenomenon in JavaScript , by which we can access the variables and functions , even before initializing it .
we are trying to access the value of variables and functions in the Memory creation phase , in this phase all variables are set to the initial value which is undefined , and in case of functions it stores the whole own function code .

// Memeory Allocation <br>
> The Memory is allocated to each `variable` and `function` , even before the JavaScript engine starts executing a single line of code .
>
>The memory is allocated only if the variables and functions are declared , If any variables and functions are not defined or declared , the result will be → Not defined .
Variables declared with “ var “ keyword and the function declaration are the part of the window object or global scope / global object / global memory .
But , the variables declared with let & const are not part of the window object or don't belong to the window object , It stores or belongs as separate memory .
And the Function expression , Anonymous function , Arrow function act as a variables , because they store in a variable and the memory is allocated to all variables , and stored as a key and set the special initial value which is undefined to all variables in the first phase of Memory creation , and any variables and functions are not present inside the function are belong to the window object or global scope / global object / global memory .
>
> So ,
The function declaration and the variable declaration with “ var “ is part of the window object / global scope / global object / global memory .<br><br>
And the variable declaration with let & const is not part of the window object , they are stored or belong  as separate memory .<br><br>
And the Function declaration , Anonymous function , Arrow function act as a variable , because they are stored in a variable and the JavaScript engine allocates the memory to all variables and stores as key and assigns the special initial values which is undefined to all variables in the first phase of Memory creation .

## Closures

Closures basically means that a function binds together with its lexical environment .

In other word →
Closure is a function together like bundled with its lexical environment .

For simplicity → 
Function along with the lexical scope forms a closure that is known as closure .

There is another definition of closures →

> Closure means that an inner function always has access to the outer function variables and parameters as well as the global variables . The inner function preserves the value of the outer function, even after the outer function has closed.

> In other words, a closure is a function having access to its parent scope, even after the parent function's execution is completed.

Its concept is deeply related to the lexical scope we just studied.


Scope chain →

> In JavaScript, when a variable is used, the JavaScript engine will seek the variable's value in its current scope . If it is unable to find the variable, it will seek the outer scope and continue this until it finds the variable or reaches global scope. If it cannot find it till the end then either it will declare the variable implicitly or will throw an error .


How does a closure look ?
>When a function is returned as a value from another function , here the closure comes into pictures .
>
>So, when a function is returned as value from another function they still maintain their lexical scope and they remember where they were actually present.

for examples, 

    function x(fname){
    var a = 7;
    function y(){
        console.log(a + ' -> ' + fname);
    }
    return y;
    }


    var z = x('Sofia');
    console.log(z); // [Function: y]
    z();            // 7 -> Sofia


For simplicit → When a function is returned as a value from another function , It not just a function code was returned but  closure also returned , and the closure enclosed the function along with its lexical scope , that was returned .

In the above code : The  y function is returned and store it at z , and when execute the z somewhere else in our program , it still remembers “ a “ , so it still remembers the reference to the “ a “ , and it tries to find out  the value of “ a “ which is 7 , then it print it , this is the closure.

## Type of function in javaScript

In JavaScript there are different types of function : 

`Function declaration` : 
Function declaration also known as function statement .
Function declarations are not executed immediately , They are “ saved for later use “ , and will be executed later , when they are invoked ( called upon ) .
Semicolons are used to separate executable JavaScript statements .
Since a function declaration is not an executable statement , it is not common to end it with a semicolon .

// syntax<br>

    function functionName(para1,para2,...paraN){
    // body of the function
    }

for example ; <br>

    function userInfo(fname,lname){
         console.log(`Hello ${fname} ${lname}`);
    }
    userInfo('Sofia','Kal');

    // output
    Hello Sofia Kal

`Function expression` : Function stored in a variable is known as function expression .
After a function has been stored in a variable , the variables can be used as a function .
Any function stored in variables do not need function names , They are always invoked (called) using the variable name .

Function expression must end with a semicolon( ; ) , because it is part of an executable statement .

// syntax<br>

    let variableName = function functionName(para1,para2,...paraN){
    // body of the function
    };

for example ; <br>

    let x = function userInfo(fname,lname){
        return `Hello ${fname} ${lname}`;
    };
    let res = x('Sofia','Kal');
    console.log(res);

    // output
    Hello Sofia Kal

`Anonymous function` : Anonymous function is a function that does not have any name .
Anonymous function must end with a semicolon( ; ) , because it is part of an executable statement .

// syntax <br>

    let variableName = function (para1,para2,...paraN){
    // body of the function
    }

for example ; <br>

    let x = function (fname,lname){
          return `Hello ${fname} ${lname}`;
    }
    let res = x('Sofia','Kal');
    console.log(res);

    // output
    Hello Sofia Kal

`Arrow function` : Arrow function is one of the features introduced in the ES6 version of JavaScript .Arrow function allows us to create a function in a cleaner way as compared to the regular function . <br><br>

However , the `this` keyword is not associated with the arrow function . Arrow function does not have its own ‘ this ‘ , so whenever we call ‘ this ‘ inside an arrow function it always refers to its parent scope / lexical scope .
Arrow function must end with a semicolon( ; ) , because it is part of an executable statement .
      
// syntax <br>

    let myFunction = (arg1, arg2, ...argN) => {
       statement(s)
    }

In the above syntax :
>myFunction is the name of the function<br>
>arg1 , arg2 , … , argN are function arguments <br>
>statement( s ) is the function body <br>

// If the body has single statement or expression , we can write arrow function as →
> let myFunction = (arg1, arg2, ...argN) => expression

// Arrow function with NO Argument →
If a function doesn’t take any argument , then we should use empty parentheses . 

>let greet = () => console.log('Hello');<br>
>greet(); // Hello

// Arrow function with one Argument → If a function has only one argument , we can omit the parentheses . 

>let greet = x => console.log(x);<br>
>greet('Hello'); // Hello

// Arrow function as an expression → We can also dynamically create a function and use it as an expression .

>let age = 5;<br>
>let welcome = (age < 18) ?( ) => console.log('Baby') : ( ) => console.log('Adult');<br>
>welcome(); // Baby

// Arrow function Multiline → If a function body has multiple statements , we need to put them inside curly brackets {  } 

>let sum = (a, b) => {<br>
>   let result = a + b;<br>
>   return result;<br>
>}<br>
>let result1 = sum(5,7);<br>
>console.log(result1); // 12

// `The 'this' with Arrow function` →
The handling of ‘ this ‘ is also different in arrow function compared to regular functions .<br><br>
Arrow function does not have its own ‘ this ‘ , so whenever we call ‘ this ‘ inside an arrow function it always refers to its parent scope / lexical scope .<br><br>
In regular functions the ‘ this ‘ keyword represents the object that called the function , which could be the window , the document , a button or whatever .
with the arrow function the ‘ this ‘ keyword always represents the parent scope / parent object .
Go for more details → https://www.w3schools.com/js/js_arrow_function.asp

Look the below examples :

// Inside a regular function →

However, this is not associated with arrow functions . Arrow function does not have its own this , So whenever you call this, it refers to its parent scope. For example : <br>

    function Person() {
    this.name = 'Jack',
    this.age = 25,
    this.sayName = function () {


        // this is accessible
        console.log(this.age);


        function innerFunc() {


            // this refers to the global object
            console.log(this.age);
            console.log(this);
        }


        innerFunc();


    }
    }

    let x = new Person();
    x.sayName();


    // output in browser
    25
    undefined
    Window { }


    // output in Node Js
    25
    undefined
    <ref *1> Object [global] { }

Here, this.age inside this.sayName( ) is accessible because this.sayName( ) is the method of an object .

However, innerFunc( ) is a normal function and this.age is not accessible because this refers to the global object (Window object in the browser). Hence, this.age inside the innerFunc( )  function gives undefined .

// Inside an arrow function →

    function Person() {
    this.name = 'Jack',
    this.age = 25,
    this.sayName = function () {


        console.log(this.age);
        let innerFunc = () => {
            console.log(this.age);
        }


        innerFunc();
    }
    }


    const x = new Person();
    x.sayName();


    // output
    25
    25

Here, the innerFunc( ) function is defined using the arrow function. And inside the arrow function, this refers to the parent's scope. Hence, this.age gives 25 .

#### Arguments Binding →

// Regular functions have arguments binding :<br>
That’s why when we pass arguments to a regular function , we can access them using the arguments keyword . for example :

    let x = function () {
        console.log(arguments);
    }
    x(4,6,7); // Arguments [4, 6, 7]

// Arrow functions `do not` have arguments binding :<br>
when we try to access an argument using the arrow function ,it will give an error. for example :

    let x = () => {
    console.log(arguments);
    }

    x(4,6,7);
    // ReferenceError: Can't find variable: arguments

To solve this issue , we can use the spread operator syntax . for example :

    let x = (...n) => {
    console.log(n);
    }

    x(4,6,7); // [4, 6, 7]

// Arrow function with `promises` and `callbacks` →

Arrow functions provide better syntax to write promises and callbacks . for example :

    // ES5
    asyncFunction().then(function() {
    return asyncFunction1();
    }).then(function() {
    return asyncFunction2();
    }).then(function() {
    finish;
    });


    // ES6
    asyncFunction()
    .then(() => asyncFunction1())
    .then(() => asyncFunction2())
    .then(() => finish);


// Things we should avoid with arrow function →

We should not use arrow functions to create methods inside objects .

    let person = {
    name: 'Jack',
    age: 25,
    sayName: () => {


        // this refers to the global .....
        //
        console.log(this.age);
    }
    }


    person.sayName();
    // output
    Undefined 

We cannot use an arrow function as a constructor .

    let Foo = () => {};
    let foo = new Foo();


    // output
    TypeError: Foo is not a constructor

`NOTE` : Arrow functions were introduced in ES6, some browsers may not support the use of arrow functions.

`Function constructor` : The function constructor is typically called with a new operator to create multiple instances of the same type . 

    function Mobile(brnad,color,price){
    this.brandName = brnad;
    this.colorName = color;
    this.priceDetail = price;
    }

    let blaclberry = new Mobile("Blackberry 9220","Silver",10000);
    let apple = new Mobile("Iphone SE", "Black",23000);

`Factory function` : A factory function is a function that returns an object known as a factory function.<br>

Factory functions create an instance object without the class & constructor function with a `new` keyword .



    function createPerson(firstName, lastName) {
        let person = Object.create(personActions);
        person.firstName = firstName;
        person.lastName = lastName;
        return person;
    }

    var personActions = {
        getFullName() {
            return this.firstName + ' ' + this.lastName;
        },
    };

    let person1 = createPerson('John', 'Doe');
    let person2 = createPerson('Sofia', 'Kal');


    console.log(person1.getFullName());
    console.log(person2.getFullName());

    // output
    John Doe
    Sofia Kal

The Factory function is rarely use in day to day life , instead we can use class or 
constructor function .
To go for more details → https://www.javascripttutorial.netjavascript-factory-functions/

`IIFE ( Immediately Invoked Function Expression )` :  Immediately invoked function expression is a function defined as an expression and executed immediately after creation . 

Syntax → <br>

    (function(){
    //...
    })();

Why IIFE →

In JavaScript any functions and variables are not defined or present inside of another function , these functions and variables belong to the global object which is a window object in the browser .

So , by using IIFE we can prevent the functions & variables  from polluting the global object .


>IIFE is a JavaScript function that is invoked as soon as it is defined .<br><br>
It is a design pattern which is also known as self-executing anonymous function and contains two major parts :<br><br>
>The first part is the anonymous function with lexical scope enclosed within the grouping operator ( ) , this prevents accessing variables within the IIFE as well as polluting the global scope .
>
>The second part is the creating immediately executing function followed by parentheses ( ).

for example ;

    (function(fname,age){
       console.log(`I am ${fname}, ${age} year old.`);
    })('Sofia',34); // I am Sofia, 34 year old.


    let a = (function(fname,age){
       console.log(`Hy i am ${fname}, ${age} year old.`);
    })('Priyanka',47); // Hy i am Priyanka, 47 year old.


    let b = ((fname,age) => {
      console.log(`${fname} here, ${age} year old.`);
    })('Sivani',29); // Sivani here, 29 year old.


By placing functions and variables inside anIIFE , we can avoid polluting them to the global object : 

    (function() {
      var counter = 0;

      function add(a, b) {
        return a + b;
      }

      console.log(add(10,20)); // 30

    }());


// Named IIFE → An IIFE can have a name , However it cannot be invoked again after execution :

Syntax : <br>

    (function namedIIFE() {
       //...
    })();


For example ; <br>

    (function ok(fname,city){
    console.log(`Hello i am ${fname} living in ${city}`);
    })('Sofia','London');

    ok();


    // output
    Hello i am Sofia living in London
    ReferenceError: ok is not defined


Go for to lean more about it → https://www.javascripttutorial.net/javascript-immediately-invoked-function-expression-iife/


---
SUMMARY : 

Function declarations or function statements are hosted and can be initialized at any time , it means we can use the function or call / invoke the function before it declares or creates .

Function expression , Anonymous function , and arrow function are also hosted but not initialized , it means we cannot use these functions before declare or create , and these functions act as variables , and undefined value is assigned to these variables in the first phase of Memory creation .

And every regular function has its own “ this “ except the arrow function . Arrow function doesn’t have its own ‘ this ‘ , it always references to the parent scope .

And the regular functions have an arguments binding with “ arguments “ keyword , but the arrow function doesn’t have argument binding .

---

## High order function 


A function that receives another function as an argument or that returns as a new function or both is called Higher-order functions . Higher-order functions are only possible because of the First-class function .

For example 1 → <br>

Functions returning another function 

    const greet = function(name){
    return function(m){


        console.log(`Hi!! ${name}, ${m}`);
    }
    }

    const greet_message = greet('ABC');
    greet_message("Welcome To GeeksForGeeks")

    // output
    Hi!! ABC, Welcome To GeeksForGeeks

`NOTE` : we can also call the function like this → greet(‘ABC’)(‘Welcome To GeeksForGeeks’) ;

For example 2 →

Passing functions as an argument 

    function greet(name){
       return `Hi!! ${name} `;
    }


    function greet_name(greeting,message,name){
       console.log(`${greeting(name)} ${message}`);
    }


    greet_name(greet,'Welcome To GeeksForGeeks','JavaScript');

    // output
    Hi!! JavaScript  Welcome To GeeksForGeeks




`NOTE` :

> The function that we pass as an argument to another function is called the callback function .
>
> Functions such as forEach( ) , filter( ) , map( ) , reduce( ) , some( ) etc . These all are examples of Higher-order functions. 

## Function first class citizens 

Functions are first class citizens in JavaScript . This means that we can store functions in variables , pass them to other functions as arguments , and we return them from other functions as values .


// Storing functions in variables →

we can treat the function like a values of other types

    function add(a, b) {
       return a + b;
    }


    let sum = add;


    // let result = add(10, 20);
    // or
    let result = sum(10,20);


    console.log(result);

    // output
    30

// Returning a function as a value from another function → 

Since functions are values , we can return a function from another function 

    function compareBy(propertyName) {
    return function (a, b) {
        let x = a[propertyName],
        y = b[propertyName];
        if (x > y) {
        return 1;
        } else if (x < y) {
        return -1;
        } else {
        return 0;
        }
    };
    }


    let products = [
    { name: 'iPhone', price: 900 },
    { name: 'Blackberry', price: 850 },
    { name: 'Sony Xperia', price: 700 },
    { name: 'Lenovo', price: 340},
    { name: 'Google pixel',price: 950}
    ];

    // sort products by name
    console.log('Products sorted by name:');
    products.sort(compareBy('name'));
    console.table(products);

    // sort products by price
    console.log('Products sorted by price:');
    products.sort(compareBy('price'));
    console.table(products);

    // output 
    Products sorted by name:
    ┌─────────┬────────────────┬───────┐
    │ (index) │      name      │ price │
    ├─────────┼────────────────┼───────┤
    │    0    │  'Blackberry'  │  850  │
    │    1    │ 'Google pixel' │  950  │
    │    2    │    'IPhone'    │  900  │
    │    3    │    'Lenevo'    │  340  │
    │    4    │ 'Sony Xperia'  │  700  │
    └─────────┴────────────────┴───────┘
    Products sorted by price:
    ┌─────────┬────────────────┬───────┐
    │ (index) │      name      │ price │
    ├─────────┼────────────────┼───────┤
    │    0    │    'Lenevo'    │  340  │
    │    1    │ 'Sony Xperia'  │  700  │
    │    2    │  'Blackberry'  │  850  │
    │    3    │    'IPhone'    │  900  │
    │    4    │ 'Google pixel' │  950  │
    └─────────┴────────────────┴───────┘


## Callback function

Callback function is a function passed as an argument to another function is known as callback function . Callback functions can be Synchronous and Asynchronous . 

I will call back late !<br>
A callback is a function passed as an argument to another function . This technique allows a function to call another function . A callback function can run after another function has finished .



    1. // Asynchronous
    2. function userName(fname,lname){
    3.   console.log(`0 - ${fname} ${lname} !`);
    4.}
    5.function personData(fn,ln,cb){
    6.   setTimeout(()=>{
    7.      cb(fn,ln)
    8.   },2000);
    9.   console.log(`1 - Hollywood`);
    10.  console.log(`2 - Black panther `);
    11.  console.log(`3 - Night Life`);
    12.}
    13.personData('Sofia','Kal',userName);

    // output
    1 - Hollywood
    2 - Black panther
    3 - Night Life
    0 - Sofia Kal !

In the above program ;
The line numbers -  9 , 10 , 11 , do not  wait for the setTimeout( ) to complete .



    1. // Synchronous
    2.function userName(fname,lname){
    3.   console.log(`0 - ${fname} ${lname}!`);
    4.}
    5.
    6.function personData(fn,ln,cb){
    7.   setTimeout(()=>{
    8.       cb(fn,ln)
    9.       console.log(`1 - Hollywood`);
    10.      console.log(`2 - Black panther`);
    11.      console.log(`3 - Nihgt Life`);
    12.   },2000);
    13.}
    14. 
    15.personData('Sofia','Kal',userName);

    // output
    0 - Sofia Kal!
    1 - Hollywood
    2 - Black panther
    3 - Nihgt Life

In the above program ;
Each line number - 9 , 10 , 11 must wait for the setTimeout( ) to complete.

`NOTE` :

> The callback function is helpful when we have to wait for a result that takes some time .
For example , the data coming for a server because it takes some time for data to arrive .
>
> The benefit of using a callback function is that we can wait for the result of a previous function call and then execute another function call.

// Look at another example : 👇 <br><br>
In this example, we are going to use the setTimeout() method to mimic the program that takes time to execute, such as data coming from the server :

    //  program that shows the delay in execution
    function greet() {
    console.log('Hello world');
    }


    function sayName(name) {
    console.log('Hello' + ' ' + name);
    }


    // calling the function
    setTimeout(greet, 2000);
    sayName('John');

    // output
    Hello John
    Hello world


As you know, the setTimeout( ) method executes a block of code after the specified time.Here, the greet( ) function is called after 2000 milliseconds (2 seconds). During this wait, the sayName('John'); is executed. That is why Hello John is printed before Hello world.

The above code is executed asynchronously (the second function; sayName( ) does not wait for the first function; greet( ) to complete).

Using a `callback function` → <br><br>
In the above example , the second function does not wait for the first function to be complete . However , if we want to wait for the result of the previous function call before the next statement is executed , we can use a callback function . For example :


    // Callback Function Example
    function greet(name, myFunction) {
       console.log('Hello world');


       // callback function
       // executed only after the greet() is executed
       myFunction(name);
    }


    // callback function
    function sayName(name) {
       console.log('Hello' + ' ' + name);
    }


    // calling the function after 2 seconds
    setTimeout(greet, 2000, 'John', sayName);


    // output
    Hello world
    Hello John

In the above program, the code is executed synchronously. The sayName( ) function is passed as an argument to the greet( ) function.

The setTimeout( ) method executes the greet() function only after 2 seconds. However, the sayName( ) function waits for the execution of the greet( ) function .


