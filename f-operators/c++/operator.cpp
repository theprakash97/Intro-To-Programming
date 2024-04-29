#include <iostream>
using namespace std;

int main(){

    // <<< Arithmetic operators
    int a = 3;
    int b = 7;
    int sum = a + b; cout << sum << endl; // 10
    int sub = a - b; cout << sub << endl; // -4
    int mul = a * b; cout << mul << endl; // 21
    int div = a / b; cout << div << endl; // 0
    int rem = a % b; cout << rem << endl; // 3

    cout << endl;

    // special operations of arithmetic 
    int x = 4;
    float y = 7;
    cout << x / y << endl; // 0.571429
    // cout << x % y << endl; // remainder operator should not be used on 'float' type
    cout << x % 13 << endl;   // 4

    cout << endl;

    // <<< Unary operators 

    // unary_plus
    int c = 4;
    int d = +c;
    cout << d << endl;

    // unary_minus
    int e = 4;
    int f = -e;
    cout << f<< endl;

    // postfix
    int current_score = 13;
    cout << current_score++ << endl; 
    cout << current_score << endl;

    // prefix
    cout << ++current_score << endl;
    cout << current_score << endl;

    cout << endl;

    // <<< Relational operators 
    int selling_price = 23;
    int cost_price = 10;

    cout << (selling_price < cost_price) << endl;
    cout << (selling_price <= cost_price) << endl;
    cout << (selling_price > cost_price) << endl;
    cout << (selling_price >= cost_price) << endl;
    cout << (selling_price == cost_price) << endl;
    cout << (selling_price != cost_price) << endl;

    cout << endl;

    // <<< Logical operators 
    string user_name = "sofia67";
    int user_age = 34;
    cout << (user_name == "sofia67" && user_age == 34) << endl;
    cout << (user_name == "sofia67" || user_age <= 18) << endl;
    cout << (!(user_name == "sofia67")) << endl;

    cout << endl;

    // <<< Assignment operators 
    int num = 17;
    num += 3; cout << num << endl;
    num -= 2; cout << num << endl;
    num *= 2; cout << num << endl;
    num /= 2; cout << num << endl;
    num %= 29; cout << num << endl;

    // <<< Bitwise operators 

    // <<< Other operators 

    cout << endl;

    // sizeof() : returns the size of data type
    cout << sizeof(float) << endl;

    // ternary
    int age = 15;
    int age_limit = 18;
    string is_eligible_for_vote = (age >= age_limit)? "yes eligible" : "not eligible";
    cout << is_eligible_for_vote << endl;

    // & : represents memory address of the operand
    string ip_address = "187:2349:458:389";
    string &get_ip_address = ip_address;
    cout << &get_ip_address << endl;

    // << : for output

    // >> : gets input 

    // '.' : accesses members of struct variables or class objects

    // -> : used with pointers to access the class or struct variables


    

    return 0;
}
/*
    output
    --------
    10
    -4
    21
    0
    3

    0.571429
    4

    4
    -4
    13
    14
    15
    15

    0
    0
    1
    1
    0
    1

    1
    1
    0

    20
    18
    36
    18
    18

    4
    not eligible
    0x7ff7bf83f2f0

*/