#include <iostream>
using namespace std;

int main(){
    string user_name = "prakash79";
    int user_age = 27;
    int age_limit = 18;

    int total_ticket = 12;
    int ticket_booked = 0;
    if(user_age >= age_limit){
        cout << "Hello " << user_name << endl;
        ticket_booked = 3;
        cout << "You booked : ";
        cout << ticket_booked << " tickets" << endl;
        cout << "Available Tickets : " << total_ticket - ticket_booked << "/" << total_ticket << endl;
    }else{
        cout << "not eligible" << endl;
    }
    
    return 0;
}