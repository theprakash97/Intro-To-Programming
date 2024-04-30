
function login_system(fname,age){
    if(fname === "theprakash" && age >= 18){
        console.log(`Hello ${fname}`);
        console.log("Sign in");
    }else if(fname !== "theprakash" && age >= 18){
        console.log(`hy ${fname}!`);
        console.log("sign up");
    }else{
        console.log("teenager not allowed");
    }
    return;
}
function main(){
    login_system("theprakash",28);
    login_system("sofia_kal",34);
    return;
}
main();