
## Iteration 

Loop statements are used to repeat a block of code multiple times. Loops are essential for automating repetitive tasks and processing on data structures . 

Loop can execute a block of code as long as a specified condition is true.
Loop can execute a block of code a number of times.Loops are handy, if you want to run the same code over and over again, each time with a different value.
There are 3 types of loops in almost all programming languages  :

| Loop statements | Descriptions | 
| --- | --- |
| for | Loop through a block of code a number of times. |
| while | Loops through a block of code while the specified condition is true. |
| do/while | Loop similar to while loop . However , the body of do..while loop is executed once before the condition is checked. |

---

## for loop statement

Loops through a block of code a number of times.
Syntax : 

> for( intiatialExpression ; testExpression ; updateExpression ) {<br>
        // code block to be executed <br>
}


Here , 

`Statement1` which is the initialExpression ,  initializes and / or declares variables and is executed only once . 

`Statement2` which is the conditionExpression that is evaluated . If the condition is true , the body of the for loop is executed . 

`Statement 3` which is the updateExpression , updates the value of the initialExpression and the condition is evaluated again and again & the process continues until  the condition is false .


>**Nested Loops** : We can place the loop inside of another loop , this is called a nested loop . The <  inner loop >  will be executed one time for each iteration of the < outer loop >.

#### Statement 1 

Normally we will use statement 1 to initialize the variable in the loop ( let i = 0 )
This is not always the case, statement 1 is optional.
We can initiate many values in statement 1 ( separated by comma ).<br>For example,<br>
> for ( let i = 0 , len = car.length , text = ‘ ‘ ; i < len ; i ++ )<br>{
       text += car[ i ] + ‘ \n ‘ ;<br>
}

And we can omit statement 1 ( like when we values are set before the loop starts ).<br>For example,<br>

>let i = 2 ;<br>
let len = cars.length ;<br>
let txt = “ “ ;<br>
for (     ;  i < len   ;   i++ ) {<br>
      text += cars[ i ] + ‘ \n ‘ ;<br>
}

#### Statement 2 

Often statement 2 is used to evaluate the condition of the initial variable.
This is not always the case, statement 2 is also optional.
If statement 2 returns true, the loop will start over again, if it returns false, the loop will end.

`NOTE` : If you omit statement 2 , you must provide a break inside the loop. Otherwise the loop will never end. This will crash your application.


#### Statement 3 
Often statement 3 is used to increments or decrements the value of the initial variable.
This is not always the case, statement 3 is also optional.
Statement 3  can do anything like negative increment  ( i - - ) , 
positive increment ( i = i + 15 ), or anything else.
Statement 3 can also be omitted ( like when we increment our values inside the loop ).<br>For example,<br>
>let i = 0 ;<br>
let len = car.length ;<br>
let txt = “ “ ;<br>
for (  ;  I < len  ;  ) {<br>
      text += cars[ i ] + ‘ \n ‘ ;<br>
      i++ ;<br>
}

## while loop statement 

The while statement loops through a block of code as long as a specified condition is true . 

Syntax :<br>

>while (testExpression) {<br>
       // code block to be executed <br>
       updation++ ;<br>
}<br>

Here , 
A while loop evaluates the textExpression inside the parentheses ( ) 
If the testExpression evaluates to true , the code inside the while loop is executed . 
The testExpression is evaluated again . 
This process continues until testExpression is false . 
When the testExpression evaluates to false , the loop stops . 

`NOTE` : Do not forget to increase the variable used in the condition , otherwise the loop will never end.

## do/while loop statement 

The do…while loop is a variant of the while loop . This loop will execute the code block once , before checking if the condition is true , then it will repeat the loop as long as the condition is true . 

Syntax :<br>

>do {<br>
       // code block to be executed <br>
       updation++;<br>
} while( testExpression ) ; <br>

Here , <br>
> - The body of the loop is executed first . Then the testExpression is evaluated .
> - If the testExpression evaluates to true , the body of the loop inside the do statement is executed again . 
> - The testExpression is evaluated once again . 
> - If the testExpression evaluates to true , the body of the loop inside the do statement is executed again .
> - This process continues until the testExpression evaluates to false . Then the loop stops . 

`NOTE` : Do not forget to increase the variable used in the condition , otherwise the loop will never end . 

## jump statements

`return`  → 
return is a reserved keyword , we can’t use it as an identifier . 
It is used to exit from a  method , with or without a value .

`break` → 
The break is a reserved keyword , we can’t use it as an identifier .
It is mainly used to terminate the loop immediately , when a certain condition is met and the control of the program moves to the next statement .

> When the break statement is used inside of two nested loops , the break statement terminates  the inner loop . 

`continue` → 
The continue is a reserved keyword , we can’t use it as an identifier . 
The continue statement is used to skip the current iteration of a loop ( for , while , do…while ) , when a certain condition is met  and the control flow of the program moves to the next iteration .
> When the continue statement is used inside of two nested loops , it skips the current iteration of the inner loop . 




