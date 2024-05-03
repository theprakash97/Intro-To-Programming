#include <iostream>
#include <math.h>
#include <string>

using namespace std;

/*
    // check list 
    - How to declare functions
    - call a function 
    - function prototype
    - type of function 
        * User-defiend function
        * Built-in functions
    - scope of variables in c++
    - function call by value
    - function call by reference
    - default parameter value 

*/

// How to declare function 
int addition(int x, int y){
    // processing 
    int result = x + y;
    return result;
}

/*
    function prototype
    --------------------
    If we want to defien a function after the function call, we need to use the function prototytpe.

*/

// prototype function 
void fun(string);

void built_in_functions(){
    // built-in functions
    cout << sqrt(64) << endl;
    cout << pow(2,4) << endl;
}

int main(){

    // call a function 
    int x = addition(10,5);
    cout << x << endl;
    fun("Prakash");
    built_in_functions();

    return 0;
}


void fun(string name){
    cout << "Are you having fun " << name << " ?" << '\n';
}