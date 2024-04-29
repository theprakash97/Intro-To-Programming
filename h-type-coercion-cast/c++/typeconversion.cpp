#include <iostream>
using namespace std;

int main(){

    /*

    // Implicit conversion :--
  - also known as 'automatic type conversion'
  - done by compiler/interpreter on its own, wihtout any external trigger from user
  - Generally takes place when in an expression more than one data type 
    is present. In such condition type conversion (type promotion) takes place to avoid lose of data.
  - All the data types of the variables are upgraded to the data type of 
    the variable with largest data type.

    bool → char → short int → int → unsigned int → long → unsigned → long long → float → double → long double

  - It is possible for implicit conversions to lose information, signs can be 
    lost (when signed is implicitly converted to unsigned), and overflow can occur (when long long is implicitly converted to float).


    */

    int x = 10;
    char y = 'a';
    // y implicitly converted to int. ASCII value of 'a' is 97 
    x = x + y;
    // x is implicitly converted to float 
    float z = x + 1.0;

    cout << x << endl;
    cout << y << endl;
    cout << z << endl;

    cout << endl;

    /*
    
    // Explicit conversion :--
  - also known as 'type casting' and it is user-defiend
  - Here the user can typecast the result to make it of a particular data type.

    In C++, it can be done by two ways:

    Converting by assignment: 
    This is done by explicitly defining the required type in front of the expression in parenthesis. This can be also considered as forceful casting.

    Syntax: (type) expression 
    where `type` indicates the data type to which the final result is converted.

    Conversion using Cast operator: 
    A Cast operator is an unary operator which forces one data type to be converted into another data type.

    C++ supports four types of casting:
    - Satic cast
    - Dynamic cast
    - Const cast
    - Reinterpret cast

    */

    float f = 3.5;
    double g = 1.2;
    int sum = (int)g + 1;
    cout << sum << endl;
    cout << (int)f << endl;


    return 0;
}
/*
    output
    --------
    107
    a
    108

    2
    3

*/