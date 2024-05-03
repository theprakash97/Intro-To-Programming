#include <iostream>
using namespace std;

// wap to print sqaures of the first 5 natural numbeers

int square(int x){
    return x * x;
}

int main(){
    for (int i = 1; i <= 5; i++){
        cout << square(i) << endl;
    }
    return 0;
}