#include <iostream>
using namespace std;

int main(){
    /*

    A Char datatype is a datatype that is used to store a single character. It is always enclosed within a single quote (‘ ‘).

    ASCII value stands for American Standard Code for Information Interchange.
    It is used to represent the neumeric value of all the characters.

    ASCII Range of 'a' to 'z' = 97 to 122
    ASCII Range of 'A' to 'Z' = 65 to 90
    ASCII Range of '0' to '9' = 48 to 57

    character_value to ascii_value :--
    To convert a character to ASCII value we have to typecast it using int(character) to get the corresponding numeric value.

    ascii_value to character_value :--
    To convert an ASCII value to a corresponding Character value we have to typecast it using char(int) to get the corresponding character value.


    */

    char sym = 'g';
    cout << sym << endl;

    // character_value to ascii_value
    char c = 'g';
    cout << "The ascii value of " << c << " is : " << int(c) << endl;

    // ascii_value to character_value
    char num = 103;
    cout << "The character value of " << num << " is : " << char(num) << endl;

    /*
        Escape Sequence in C++ 
        --------------------------
        Escape sequences are characters that determine how the line should be printed on the output window. The escape sequence always begins with a backslash ‘\’ (also known as an escape character). Some Examples of Escape Sequences are mentioned below: 

        \n  :  newline
        \\  :  backslash
        \t  :  horizontal tab
        \v  :  vertical tab
        \0  :  null character

    */

    char m = 'P';
    char n = '\t';
    char o = 'R';
    char p = '\t';
    char q = 'A';
    char r = '\n';
    string user_name = "my name start with (pra + kahs)";
    cout << m << n << o << p << q << r << user_name << endl;


    return 0;
}

/*
    output
    ---------
    g
    The ascii value of g is : 103
    The character value of g is : g
    P       R       A
    my name start with (pra + kahs)

*/
