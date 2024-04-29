
## Type Coercion

Type coercion refers to the automatic conversion of values from one data type to another data type, typically performed during operations or comparisons involving different data types. By using type coercion, JavaScript attempts to make the data types compatible to complete the operation or comparison .

## Type Casting/Conversion


The conversion of one data type into another data type is known as type conversion or  type casting . 

In a programming there are two types of type conversion :
Implicit conversion ( Implicit casting  or Widening casting ) 
Explicit conversion ( Explicit casting or Narrowing casting ) 


Data types do not have the same level , that means ordering of data types is not the same .  some of the data types have Higher-order and some of the data types have Lower-order . 

`Implicit conversion or Implicit Casting ( Widening casting )`  → <br>
The conversion from Lower data types into Higher data types is called Implicit conversion . It is done automatically by the interpreter or compiler , since the conversion is from Lower data types into Higher  data types to prevent data loss . 

`Explicit conversion or Explicit Casting ( Narrowing casting )` → <br>
The conversion from Higher data types into Lower data types is called Explicit conversion ( Explicat casting )  . It must be done manually via programmer by using 2 tricks : 
placing the type in parentheses in front of the value , or 
some programming languages use built-in methods , In python : 
int( ) , float( ) , str( ) , ord( ) , hex( ) , oct( ) , list( ) , tuple( ) , set( ) , dict( ) , etc for the type casting in Python . 

Abd In Explicit casting ( Explicit conversion ) , since the conversion from Higher data types  into Lower data types type , during this process data may be loss . 


NOTE : While performing any operations on variables with different data types , one of the variable’s data types will be changed to the Higher-order data types , according to the level . 

**Implicit conversion ( implicit casting / widening casting ) :** <br>
> Small →  large<br>
> automatic type conversion <br>
> Converting a smaller type to larger type size <br><br>
> byte → (short,char) → int → long → float → double → object 


**Explicit conversion ( explicit casting / narrowing casting ) :** <br>
> large →   Small<br>
> manually type conversion <br>
> Converting a larger type to a smaller type size<br><br>
> object → double → float → long → int → (short,char) → byte




