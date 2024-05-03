#include <iostream>
using namespace std;

    // Given two numbers 'a' and 'b', wap to print all the prime numbers present between 'a' and 'b'

bool is_prime(int num){
    // function checks if the number is prime number or not 
    for(int i = 2; i <= (num - 1); i++){
        if(num % i == 0) return false;
    }
    return true;
}

bool is_prime_btr(int num){
    for(int i = 2; i * i <= num; i++){
        // i^2 <= num --> i <= sqrt(num)
        if(num % i == 0) return false;

    }
    return true;
}

int main(){
    int a = 2, b = 10;
    for(int i = a; i <= b; i++){
        if(is_prime(i)){
            cout << i << " ";
        }
    }
    cout << endl;

    cout << endl;

    int c = 2, d = 40;
    for(int i = c; i <= d; i++){
        if(is_prime_btr(i)){
            cout << i << " ";
        }
    }
    cout << endl;
    return 0;
}

/*
    output
    ---------
    2 3 5 7 

    2 3 5 7 11 13 17 19 23 29 31 37 
    
*/