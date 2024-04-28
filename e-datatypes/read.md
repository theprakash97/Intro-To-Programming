## Index 

> - What is data 
> - What is data types 
> - What is data structures 
> - data types Vs data structures
> - primitive Vs non-primitive data structures 
> - Data types in C++, Python , JavaScript 
> - Advantages & Dis-advantages 

## What is data 

Data are the raw facts , unorganized facts that need to be processed. Data can be something simple & random and useless until it is organized. Data can be any form :

       Single character
       Boolean ( true or false )
       Text ( string )
       Number ( integer or float or double or complex )
       Pictures
       Sound
       Video

In a computer's storage , digital data is a sequence of bits ( binary digits ) with a value of 1 & 0. Data is processed by the cpu . In computer science, each piece of data is associated with a certain type often called data types .

## What is data types

In computer science, a data type is basically a way to categorize different kinds of data. It defines what type of information a variable can hold and the operations that can be performed on it .  It specifies the different types & sizes of data that can be used in programs. Such as numbers, strings, and booleans etc .


Data types also tell us more information about : 

> - Specifies the kind of data the variable can store. For example , an integer data type can only hold whole numbers, while a string data type can store text. 
> - Specify the  maximum and minimum range of a particular data . 
> - Control what kind of operation to be performed on a particular data of variable . 
> - Different data types take up different amounts of space in the computer’s memory . 


A data type serves as a categorization of data, defining the specific type of value that can be stored in a variable or expression. 

## What is data structures

A data structure is a particular way of organizing data in a computer memory, so that it can processing, retrieving , updating and manipulate data in very efficient manner in terms of `time` & `space` complexities of different tasks.

In computer science, data strucutres are broadly divided into 2 types :--

> 1) Primitive Data Strucure 
> 2) Non-primitive Data Strucutre

`Primitve data structures : ` 
> Primitve data strucutres are basic or primary/fundamental data strucutres.<br>
> Primitive data strucutres are built-in types and the size already defined and fixed.<br>
> Primitve data structures allow to store only single data. <br>
> Primitive data types hold only a single data type value & they are addressed by  value.<br>
> Primitive data types can’t have properties and methods , But some programming languages has implemented the primitive data types as Wrapper Classes  ( example : Java , JavaScript ) and added some additional properties and methods to them, which work like an object.<br>


Primitve data structures are : 

| Data | Example | Type | Size (Memory Allocation) |
| --- | --- | --- | --- |
| textual | hi prakash! | is associated with `string` type | 4 bytes for each character (unicoe)|
| 26 | age | is associated with `byte` type | 1 byte (8 bits) |
| 35000 | phone_price | is associated with `short` type | 2 bytes (16 bits) |
| 570000 | car_price | is assocaited with `int` type | 4 bytes (32 bits) |
| 1109284847482948 | bank_account_no | is associated with `long` type | 8 bytes (64 bits) |
| 5.6 | user_height | is associated with `float` type | 4 bytes (32 bits) |
|73.9999999 | stock_price | is associated with `doube` type | 8 bytes (64 bits) |
| a,A,0,?,_,etc | symbol, letter, character | is associated with `char` type | 2 bytes (16 bits) |
| ture/false | is_active_now | is associated with `boolean` type | 1 bytes |

`Non-primitive data strucutres : `
> Non-primitve data structure are derived types as they are derived from primary or primitive data types by performing various operations on top of them.<br>
> Non-primitive data strucutre allow to store mulitple collections of data of same type or different types either in a contiguous or random location stores in memory.<br>
> Non-primitive data structures hold large amount of data, often represents complex data strucutres. some non-primitive data structures are comes with programming language by default (built-in) and some other non-primitve data structures we have to code them if we want to use them.<br>
built-in non-primitve data strucutres are : Array(List), String , Map(Dictionary),Set .<br>
custom/user-defined non-primitive data strucutres are : Class, Linkedlist , Stack , Queue, etc.<br><br>
> Non-primitive data structure further divided into 2 groups :--<br>
> - Linear data structure  : Array , Linkedlist , Stack , Queue 
> - Non-linear data structure  : Tree , Graph , Table , Set

Non-primitive data types hold multiple collections of value & these data types are addressed by the memory address of the variable.

| Language | Built-in data structures | user-defined data structures | 
| --- | --- | --- |
| c++ | Function<br>Array<br>String<br>Pointer<br>Reference | Class<br>Structure<br>Union<br>Enumeration<br>Typedef |
| python | List<br>Tuple<br>Dictionary<br>Set<br>File| Class |
| javascript | Array<br>Object<br>Map<br>WeakSet<br>Set<br>WeakSet | Class |

---

## Here general overviews of data types :

In programming , data types act like labels that define the kind of information a variable can hold . They basically tell the compiler what type of data to expect and how to work with it.

| Data types | Explanations |
| --- | --- |
| Basic/primitive | These are the fundamental building blocks that store single values.<br>`Integer :` Represents whole numbers (positive, negative, or zero). Examples: age, count, ID number.<br>`Floating-point :` Represents numbers with decimal points for real numbers. Examples: scientific measurements, pi (3.14...).<br>`Boolean :` Represents logical values, either true or false. Examples: isLoggedIn, isActive.<br>`Character :` Represents a single character (letter, number, or symbol). Examples: initial of a name, a key press.|
| Composite | These are built on top of basic data types to store more complex data structures.<br>`String :` Represents a sequence of characters, like text. Examples: name, address, sentence.<br>`Array :` An ordered collection of items of the same data type. Examples: list of names, scores in an exam.<br>`Structures (or structs) :` Groups related data variables of different types under a single name, like storing information about a person (name, age, address).|
| User-defined |In some languages, you can create your own data types based on your specific needs. This allows for more complex data organization and manipulation. Examples include :<br>`Classes :` Blueprints for creating objects that encapsulate data (attributes) and functionalities (methods).<br>`Enumerations (enums) :` Assigning names to integer constants, making code more readable (e.g., days of the week as Monday, Tuesday, etc.).|

Here these are some of the most common data types found in programming languages. The choice of data type depends on the requirements of the program and the operations that need to be performed on the data :--

| Data types | Descriptions | 
| --- | --- |
| Integer (int) | Represents the whole number without any fractional component.<br>Can be signed ( positive, negative or zero ) or unsigned ( only positive or zero )<br>Sizes vary depending on programming language and system architecture ( e.g : 32-bit, 64-bit integers ).<br>Examples : 1 , -5 , 79 , etc.|
| Floating-point( float , double ) | Represents real numbers with fractional parts.<br>They are particularly useful when dealing with values that cannot be accurately represented by integers, such as : scientific measurements, financial calculations , and graphical data.<br>Typically stored in IEEE754 format.<br>Size varies depending on the programming language ( e.g : single precision(float 32 bits) , double precision( double 64 bits) ).<br>Examples : 3.14 , -0.5 , 1.72345567849 , etc. |
| Boolean (bool)  | Represents a binary value that can be either true/false.<br>Used in logical operations, conditional statements, and boolean algebra.<br>Typically takes up 1 byte of memory.<br>Examples : true, false. |
| Character (char) | Represents a single character.<br>Enclosed in single quotes ( ‘ ‘ ).<br>Typically takes up 1 byte of memory.<br>All characters are encoded by the most popular encoding standard ( ASCII / UNICODE ).<br>Examples : ‘a’ , ‘B’ , ‘$’, ‘#’, etc. |
| String (str) | Represents a sequence of characters.<br>Enclosed in double quotes( “  “).<br>May be implemented as an array or a specialized data structure.<br>Examples : “hello” , “world” , “12345” , etc. |
| Array | Represents a collection of elements of the same data type.<br>Elements are stored in contiguous memory locations.<br>Size is fixed or dynamically resizable depending on the programming language.<br>Accessed using index notation.<br>Examples : [ 1 , 2 , 3 , 4 ] , [ “apple” , “banana” , “orange” ] |
| Struct (Structure) | Represents a collection of variables (fields) grouped together under one name.<br>Fields can have different data types.<br>Allow for the creation of custom data types.<br>Examples : struct Person { string name; int age; }. |
| Pointer  | Stores memory addresses of other variables or data structures.<br>Allows for dynamic memory allocation and manipulation.<br>Can be used for efficient memory management and data structures like : Linkedlist , Trees, etc.<br>Examples : int* ptr ; // pointer to an integer |
| Enumeration (enum) | Represents a set of named integer constants.<br>Provides a way to define symbolic names for integer values.<br>Help improve code readability and maintainability.<br>Examples : enum Color { RED, GREEN, BLUE } ; |
| void | Represents the absence of a specific type.<br>Often used as the return type of functions that do not return a value.<br>Can also be used to indicate generic or unspecified types.<br>Examples : void, void* (generic pointer ) |

## Data types Vs Data structures

| Data Types | Data Structures | 
| --- | --- |
| A data type serves as a categorization of data, defining the specific type of value that can be stored in a variable or expression . | On the other hand, a data structure is a way of organizing and storing data in computer memory , ensuring efficient excess and manipulation of the stored information .|
| int , float , char , string , boolean | Stack, Queue , Linkedlist , Tree , Graph , Table , Set , etc. | 
| No algorithmic time complexity | Involve algorithmic time complexities |
| Direct assignment of value | Operations for entering data |
| Abstract programming | Concrete programming |

## Primitive Vs Non-primitive data structures

| Primitive data structures | Non-primitive data structures |
| --- | --- |
| Primitive data structure is the data structure that allows to store only single data type value. | Non-primitive data structures is a data structure that allows storing multiple data types values of the same type or the  different types. |
| integer, boolean, characters, float , etc. | Array, Linkedlist , Stack , Queue , Tree, GrapH , Table , Set. |
| Primitive data structures always contain some value, these data structures do not allow storing NULL values. | We can store a NULL value in the non-primitive data structures. |
| The size of primitive data structures is dependent on the type of the primitive data. | The size of non-primitive data structures is not fixed. |
| Primitive data types are immutable. | Non-primitive data types are mutable. | 

## Data types in C++, Python , JavaScript

| Language | Explanation | 
| --- | --- | 
| c++ | `Primitive data types are basic or fundamental data types` , they come with programming languages by default and the sizes are already defined and fixed size.<br>Primitive data types store single data of a single type.<br><br>Primitive data types are :--<br>Integer ( int )<br>Floating<br>point ( float ) <br>Double floating point ( double )<br>Boolean ( bool )<br>void<br>Character ( char )<br>Wide character ( wchar_t )<br>Undefined<br>Null<br><br>`Derived data types` that are derived from the primitive or built-in data types by applying some operation on top of them. <br><br>Derived data types are :-- <br>Function<br>Array<br>Pointer<br>Reference<br><br>`Abstract or User-defined data types` are created by the user itself as per specific needed.<br><br>Abstract or User-defined data types are :--<br>Class<br>Structure <br>Union<br>Enumeration<br>Typedef |
| pyhton | Since everything is an object in python programming, data types are actually classes and variables are instances ( objects ) of these classes.<br><br>Python has various standard/built-in data types :--<br> <br>Text type        → str<br>Numeric type     → int , float , complex<br>Boolean type     → bool<br>None type        → NoneType<br>Sequence type    → string, list , tuple , range<br>Mapping type     → dict<br>Set type         → set<br>Binary type      → bytes , bytearray , memoryview<br><br>`primitive data types` : int , float , str, boolean<br>`non-primitive data types` : Array, List, Tuple, Dictionaries , Set , File<br>`Immutable Objects` : int , float, str, bool , complex, tuple, bytes, forzenset<br>`Mutable Objects` : list, dic, set, bytearray |
| javaScript | JavaScript has a total 8 data types, out of 8 , the seven are primitive data types and the remaining one is an object type ( also known as reference or Non-primitive types ). <br><br>`primitive data types are` :  string, number, boolean , bigInt , symbol , undefined , and null.<br>`object or non-primitive types are` :  Array, Object, Function, Date, RegExp, Math, Map, Set, Class, Interface, etc. | 

## Advantages & Dis-advantages

| Adavantages | Data types provide a way to categorize and organize data in a program, making it easier to understand and manage.<br>Each data type has a specific range of values it can hold, allowing for more precise control over the type of data being stored.<br>Data types help prevent errors and bugs in a program by enforcing strict rules about how data can be used and manipulated.|
| --- | --- | 
| Dis-advantages | Using the wrong data type can result in unexpected behavior and errors in a program.<br>Some data types, such as long doubles or char arrays, can take up a large amount of memory and impact performance if used excessively.| 

---


