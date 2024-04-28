#include <iostream>
using namespace std;

// space ship programs 

 void start_space_ship(){
        cout << "ship has been started" << endl;
        cout << "ready to fly..." << endl;
}

class SpaceShip {       // The class
  public:               // Access specifier
    int number_of_crew; // Attribute (int variable)
    string ship_color;  // Attribute (string variable)
};

int main(){

    /* <<< PRIMITIVE DATA TYPES >>> */

    // Integer ( int ) 
    int no_of_space_crew = 7;
    cout << no_of_space_crew << endl;

    // Floating point ( float ) 
    float total_fuel = 250.7;
    cout << total_fuel << endl;

    // Double floating point ( double ) 
    double miles_per_second = 2.339999999;
    cout << miles_per_second << endl;

    // Boolean ( bool ) 
    bool is_hydrogen_liquid = true;
    cout << is_hydrogen_liquid << endl;

    // void : absent of data type (often used with function)

    // Character ( char ) 
    char is_water_supply_active = 'y';
    cout << is_water_supply_active << endl;

    // Wide character ( wchar_t ) 
    wchar_t is_main_engine_start = 'n';
    cout << is_main_engine_start << endl;

    cout << endl;

    /* <<< DERIVED DATA TYPES >>> */

    // Function
    start_space_ship();

    // Array
    string mission_path[4] = {"moon","explore universe","mars","venus"};
    cout << mission_path[2] << endl;

    // Pointer : get the memory address of a variable by using the `&` operator
    string longet_path_mission = "Venus";
    cout << longet_path_mission << endl;
    cout << &longet_path_mission << endl; // Outputs the memory_ address


    // Reference : A reference variable is a "reference" to an existing variable, and it is created with the `&` operator
    string target_mission_tonight = "Moon";
    string &space_ship = target_mission_tonight;
    cout << target_mission_tonight << '\n';
    cout << space_ship << '\n';

    cout << endl;


    /* <<< USER-DEFINED DATA TYPES >>> */

    SpaceShip lunar_jet;  // Create an object of SpaceShip

     // Access attributes and set values
    lunar_jet.number_of_crew = 7; 
    lunar_jet.ship_color = "Silver";

     // Print attribute values
    cout << lunar_jet.number_of_crew << '\n';
    cout << lunar_jet.ship_color << '\n';

    return 0;
}
/*
    output
    --------
    7
    250.7
    2.34
    1
    y
    110

    ship has been started
    ready to fly...
    mars
    Venus
    0x7ff7b2c712e0
    Moon
    Moon

    7
    Silver

*/