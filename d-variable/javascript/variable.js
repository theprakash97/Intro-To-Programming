
function variable_concept(){
    let user_age = 27;
    let user_height = 5.6;
    const user_name = "theprakash97";
    const GENDER = 'M';
    let is_active_now = false;

    console.log(user_age);
    console.log(user_height);
    console.log(user_name);
    console.log(GENDER);
    console.log(is_active_now);

    console.log();

    // assignment 
    user_age = 30;
    console.log(user_age);
    user_age *= 2;
    console.log(user_age);

    console.log();

    // set initial value
    let game_score = 0;
    game_score += 3;
    game_score += 9;
    console.log(`final score is : ${game_score}`);

    console.log();

    // string initial value
    let ip_address = "";
    ip_address = "188";
    ip_address += "0:495";
    ip_address += ":4985";
    console.log(ip_address);
    console.log(typeof(ip_address));
    console.log(typeof(34));

    return;
}

function main(){
    variable_concept();
    return;
}
main();

/*
    output
    -------
    27
    5.6
    theprakash97
    M
    false

    30
    60

    final score is : 12
    
    1880:495:4985
    string
    number

*/