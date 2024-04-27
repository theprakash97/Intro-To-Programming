/*
    To know about programming syntax 

    ...
    author : prakash
    data   : 27/apr/2024
    ...
*/

/*
    // Syntax :--
    Syntax refers to specific rules and structures of the programs, which are used to write codes/instructions 
    with the help of programming languages . The syntax can vary depending on programming languages . 

    Syntax        Descriptions
    ----------- + ------------------------------------------------------------------------------------
    String        Represents textual data, typically written within double quotes.
    number        Represents numeric values, typically written without quotes.
    boolean       Represents logical entity, either true/false 
    void          Absence of data type and often used with functions, specify the function doesn’t return 
                  any value to the place where the function is begin called . 
    character     Represents single letter, digit, any symbols and  
                  typically written within a single quote.
    Indentation   Refers to white space at the beginning of code-line to indicate block of codes and define 
                  the scope of control statements, functions, classes.
    Literals      Represent fixed values/raw data that can be assigned to variables, passing as arguments to functions.
                  Typically it's hard_coded values without getting data from the user/terminal . 
    main()        The entry point of a program, where all the statements start execution.
    ( )           Represents parentheses, It has different meaning based on different context :=
                  - the context of function definition, it used enclosed parameters . 
                  - the context of function call, it used to call a function by passing  with or without arguments . 
                  - the context of expression, it used to define precedence . 
                  - the context of control-flow statements, it used to check conditions, returning boolean 
                    values either true/false.
    {  }          Represents a pair of curly braces, used to define dictionaries,set data types in context of 
                  python programming. But in the context of c++, javascript it will be different.
    [ ]           Represents square bracket, it used to define array data type.
    ;             Represents semicolon, it is used to terminate the statements, also used to separate 
                  multiple statements on single-line.
    ,             Represents comma operator, it used to separate multiple identifiers in variable declaration, 
                  also used to make chain statements together inside `for loop`.
    .             Represents dot operator, it used to separate module_name from classes, functions, variables, 
                  etc. Also used to separate variables , methods from a reference_variable and class .

    #             Single-line comment in python.

    ‘’’  
    ‘’’ 
    or            Multi-line comments in python. 
    “”” 
    “””

    Identifiers   Identifiers are names, given to an entity in a program, the entity could be ; variableName
                  , functionName, className, packageName, labelName.

                  The general rules for naming variables , methods , package & classes are :
                  * Names can only contain alpa-numeric characters , underscores ( A-z,0-9,_  ) . 
                  * Names cannot start with a number and must begin with either :  letter or underscore or 
                    dollar sign . 
                  * Names should start with a lowercase letter and it cannot contain whitespace . 
                  * Names are case sensitive ( ‘ myAge ‘ and  ‘ myage ‘ are different variables ) . 
                  * Reserved words cannot be used as names ( Identifiers ).

                  * The names of variables , methods , classes , packages with more than one word can be difficult 
                    to read .  There are several techniques you can use to make them more readable :

                    Camel case : Each word  starts with a capital letter , except the first character of first word :--
                        > String firstName = ‘John’ 
                    Pascal case : Each word starts with a capital letter :--
                        > String FirstName = ‘John’ ;
                    Snake case : Each word is separated by an underscore character :--
                        > String first_name = ‘John’ ;

    Keywords        Keywords are predefined and reserved words , they have a special meaning/purpose to the 
                    compiler/interpreter.
    Comments        The comments are used to explain the codes; about what the code does, how it works.
                    Comments can also be used to prevent the execution, when testing alternative code.
    Indentation     Indentation refers to the white-space at the beginning of a code line. Where in other 
                    programming languages the indentation in  code is for readability only , the indentation in python is very important. Python uses the indentation to define a block scope / block of code, the block of conditions , loops , functions , classes .

                    Python indentation tells the python interpreter that the groups of statements belong to a particular block of code . In python , indented code blocks are always preceded by a colon ( : ) on the previous line.

                    Indentation rules :
                    - we have to use the same number of spaces in the same code block , otherwise the python 
                      will give an error .
                    - python will give an error if we skip the indentation .
                      the number of spaces is up to us as a programmer , the mostly used 4 spaces , but it has to be 
                      at least one .

                    In python, the indentation is very important.

    In python       Python uses a new line to complete a command , whereas other programming languages  
                    use the semicolons (;) to terminate the statement / complete a command .

                    By default , in python the end of a statement is marked by a newline character.But we can make the statements extend over multiple lines by using the line continuation character.

                    The line continuation character specified into two way :

                        Implicitly line continuation → ( ) , [  ] ,  {  }
                        explicitly line continuation → \

                    Multiple statement are allowed to one line when separated by semicolons ( ; )

    end.
*/