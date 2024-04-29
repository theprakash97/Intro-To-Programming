const prompt = require("prompt-sync");
const sc = prompt();

function user_input(){
    let user_firstname = sc("enter your firstname : ");
    let user_age = parseInt(sc("enter your age : "));
    console.log(`Hello mr/miss ${user_firstname} ! Are you ${user_age} year old?`);
    return;
}
function main(){
    user_input()
    return
}
main();

/*
    output
    -------
    enter your firstname : Prakash
    enter your age : 27
    Hello mr/miss Prakash ! Are you 27 year old?

*/