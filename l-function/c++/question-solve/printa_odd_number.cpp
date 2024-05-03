#include <iostream>
using namespace std;

    // Given two numbers 'a' and 'b', wap using functions to print all the odd numbers between 1 to 10

bool is_odd(int num){
    if(num % 2 == 0){
        // number is even
        return false;
    }else{
        // number is odd 
        return true;
    }
}
int main(){
    int a = 1, b = 10;
    for(int i = a; i <= b; i++){
        if(is_odd(i)){
            cout << i << endl;
        }
    }
    return 0;
}

/*
    output
    --------
    1
    3
    5
    7
    9
    
*/