#include <iostream>
#include <string.h>
#include <typeinfo>

using namespace std;

int main(){
    
    int user_age = 27;
    float user_height = 5.6;
    string user_name = "theprakash97";
    char GENDER = 'M';
    bool is_active_now = false;

    cout << user_age << endl;
    cout << user_height << endl;
    cout << user_name << endl;
    cout << GENDER << endl;
    cout << is_active_now << endl;

    cout << endl;

    // assignment 
    user_age = 30;
    cout << user_age << endl;
    user_age *= 2;
    cout << user_age << endl;

    cout << endl ;

    // set initial value 
    int game_score = 0;
    game_score += 3;
    game_score += 9;

    cout << "final score is : " << game_score << endl;

    cout << endl;

    // string initial value
    string ip_address = "";
    ip_address = "188";
    ip_address += "0:495";
    ip_address += ":9485";
    cout << ip_address << endl;
    cout << typeid(ip_address).name() << endl;
    cout << typeid(34).name() << endl;
    return 0;
}
/*
    output
    --------
    27
    5.6
    theprakash97
    M
    0

    30
    60

    final score is : 12
    
    1880:495:9485
    NSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
    i

*/