
# space ship programs

def main():

    '''PRIMITVE DATA TYPES'''
    # int 
    no_of_space_crew = 7
    print(no_of_space_crew,type(no_of_space_crew))

    # float 
    total_fuel = 250.7
    print(total_fuel,type(total_fuel))

    # bool
    is_hydrogen_liquid = True
    print(is_hydrogen_liquid,type(is_hydrogen_liquid))

    # character
    is_water_supply_active = 'y'
    print(is_water_supply_active,type(is_water_supply_active))

    # str
    target_mission_tonight = "Moon"
    print(target_mission_tonight,type(target_mission_tonight))

    # complex 
    a = 4 + 5j
    print(a,type(a))

    # None
    get_moon_temperature = None
    print(get_moon_temperature,type(get_moon_temperature))
    

    # range
    time_count = range(0,9)
    print(time_count,type(time_count))

    print()

    '''NON-PRIMITIVE DATA TYPES'''
    # list 
    mission_path = ["moon","explore_universe","mars","venus"]
    print(mission_path[2],type(mission_path))

    # tuple 
    capture_speed_per_hours = (1200,780,2500,1200,1250,1873,2500)
    print(capture_speed_per_hours,type(capture_speed_per_hours))

    # dict
    space_ship = {
        "no of crew" : 7,
        "color" : "silver",
        "path" : ["moon","venu","mars"]
    }
    print(space_ship["path"][1],type(space_ship))

    # set 
    space_ship_checking = {"door","engine","fuel","support_tank"}
    print(space_ship_checking,type(space_ship_checking))

    return

main()

'''
    output
    ------
    7 <class 'int'>
    250.7 <class 'float'>
    True <class 'bool'>
    y <class 'str'>
    Moon <class 'str'>
    (4+5j) <class 'complex'>
    None <class 'NoneType'>
    range(0, 9) <class 'range'>

    mars <class 'list'>
    (1200, 780, 2500, 1200, 1250, 1873, 2500) <class 'tuple'>
    venu <class 'dict'>
    {'support_tank', 'door', 'fuel', 'engine'} <class 'set'>

'''