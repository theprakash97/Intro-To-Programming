
## Operators

Operators are special symbols used to perform operations on values of variable or literal values. Such as addition, subtraction, and comparison .

Operators are used to manipulate data in programs.

| Operator name | Descriptions | Symbols |
| --- | --- | --- |
| Arithmetic | Arithmetic operators are used to perform simple mathematical operations on primitive data types | +, - , * , / , %|
| Unary | Unary operators are used with only one operand. | +, - , ++ , - - |
| Comparison | Comparison operators compare two values and return a boolean value, either true/false . These operators are used to check for relations like : equality , greater than , less than, they return boolean results after the comparison and extensively used in looping statements as well as conditional if…else statements. | > , >= , < , <= , == , === , != , !== |
| Logical | Logical operators are used to perform operations on more than two conditions and return a boolean value after evaluating the condition.<br>Logical operators are used in decision making ( if…else / else…if ) <br>`If ( condition1 && condition2)` → If the condition1 is false then the compiler won’t check for condition2.<br>`If ( condition1 or condition2)` → If the condition1 is true , then the compiler won’t check for condition2,If the condition1 is false , then the compiler will check for condition2. | && , or , ! |
| Ternary | Ternary operator is the shorthand version of the if…else statement . It has 3 components and hence the name is ternary. | Expression ? expression1 : expression2; |
| Bitwise | Bitwise operators are rarely used in everyday programming | & ( Bitwise AND )<br> or( Bitwise OR  ) <br>^  ( Bitwise XOR ) <br>~   ( Bitwise NOT ) <br><< ( Left shift ) <br> >> ( sign-propagation shift ) <br> >>> ( zero-fill right shift ) |
| Assignment | Assignment operators are used to assign a value to the variable. | =<br>+=<br>-=<br>*=<br>/=<br>%= |
| Comma (,) | Evaluates multiple operands and returns the value of the last operand. | let a = ( 1, 3, 4 ) ; // 4 |
| delete | Deletes an object’s property, or an element of an array | delete x ; |
| typeof | Return a string indicating the data type | typeof 3 ; // number |
| void | discards the expression’s return value | void( x ) |
| in | Returns true if the specified property is in the object | property in object |
| instanceof | Return true if the specified object is of the the specified object type | object instanceof object_type |

## Operator Precedence

Operators precedence describes the order in which operators will be evaluated first in expressions . while the associativity in other hands, determines the direction ( typically direction occurs either left to right or right to left ) of operators if the multiple operators have the same precedence in expressions . 

Operators are typically used to manipulate data of variables or literal values in programs . 

Operators with highest precedence are evaluate first : 

| Level | Operator | 
| --- | --- | 
| 15 | ( ) |
| 14 | ** | 
| 13 | ++,-- (postfix) |
| 12 | ++,-- (prefix) |
| 11 | +,- (unary_plus, unary_minus) |
| 10 | *, /, //, % |
| 9 | +, - (addition, subtraction) | 
| 8 | ==, !=, <, <= , >, >=, is, is not, in, not in |
| 7 | not ( logical NOT ) |
| 6 | and ( logical AND ) | 
| 5 | or  ( logical OR ) |
| 4 | ?:, =, :, +=, -=, *=, **=, /=, %=, ( Assignment )|
| 3 | , ( comma ) |

If two operators have the same precedence, the expression is evaluated from left to right.<br><br>
for example :<br>
> print(5 + 4 - 7 + 3) # 5

---








