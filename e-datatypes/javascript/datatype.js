
// space ship programs


function main(){

    // <<< PRIMITIVE DATA TYPES >>> 
    
    // Integer
    let no_of_space_crew = 7;
    console.log(no_of_space_crew,typeof(no_of_space_crew));

    // Floating-point (64 bits)
    let total_fuel = 250.7;
    console.log(total_fuel,typeof(total_fuel));

    // Boolean
    let is_hydrogen_liquid = true;
    console.log(is_hydrogen_liquid,typeof(is_hydrogen_liquid));

    // character 
    let is_water_supply_active = 'y';
    console.log(is_water_supply_active,typeof(is_water_supply_active));

    // String 
    let target_mission_tonight = "Moon";
    console.log(target_mission_tonight,typeof(target_mission_tonight));

    // undefined 
    let get_distance = undefined;
    console.log(get_distance,typeof(get_distance));

    // null 
    let moon_current_temperature = null;
    console.log(moon_current_temperature,typeof(moon_current_temperature));

    // bigint
    let distance_earth_to_moon = 3944958999999999934585939535n;
    console.log(distance_earth_to_moon,typeof(distance_earth_to_moon));

    // symbol
    let get_engine_temperature = Symbol("ent");
    console.log(get_engine_temperature,typeof(get_engine_temperature));

    console.log();

    // <<< DERIVED DATA TYPES >>>

    // Array
    const mission_path = ["moon","explore_universe","mars","venus"];
    console.log(mission_path[2],typeof(mission_path));

    // Object
    const space_ship_info = {
        'no of crew' : 7,
        color : 'silver',
        path : ["moon","explore_universe"]
    };
    console.log(space_ship_info.path[1],typeof(space_ship_info));

    // Map

    // Set 

    return;
}
main();
/*
    output
    --------
    7 number
    250.7 number
    true boolean
    y string
    Moon string
    undefined undefined
    null object
    3944958999999999934585939535n bigint
    Symbol(ent) symbol

    mars object
    explore_universe object

*/