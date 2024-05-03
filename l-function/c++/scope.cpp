#include <iostream>
using namespace std;

// global variable
string user_name = "Prakash";

void fun(){
    // local variable
    int x = 10;
    for(int y = 0; y < 5; y++){
        x = x + y;
        int z = x * x;
    }
    cout << x << endl;
    // cout << y << endl;
    // cout << z << endl;
    cout << user_name << endl;
    // 
}
int main(){
    cout << user_name << endl;
    user_name = "sofia_kal";
    fun();
    return 0;
}