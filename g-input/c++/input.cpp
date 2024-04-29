#include <iostream>
using namespace std;

int main(){
    cout << "enter your firstname : ";
    string user_firstname = "";
    cin >> user_firstname;
    cout << "enter your age : ";
    int user_age;
    cin >> user_age;

    cout << "firstname : " << user_firstname << endl;
    cout << "age : " << user_age << endl;

    return 0;
}
/*
    output
    -------
    enter your firstname : Prakash
    enter your age : 27
    firstname : Prakash
    age : 27
    
*/