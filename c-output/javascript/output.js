
/*
    To output something to the console, JavaScript has built-in object that is `console` along with `log()` method to produce final output.

    Syntax : console.log('message');

    NOTES : The `console.log()` add a new line at the end after priting the message by default.
*/

function main(){
    console.log("Hello world");
    console.log(4 + 5);
    console.log("4 + 5");
    console.log(4 > 9);
    console.log(`I am prakash behera`,27,"year old!");
    let num = 7;
    console.log(3 > 9,"hy",num += 3);
    console.log(num = -79);
    console.log("Hy\nare you comming tonight!");
    console.log(); // empty line
    console.log("JavaScript is amazing!");
    return
}
main();
/*
    output
    --------
    Hello world
    9
    4 + 5
    false
    I am prakash behera 27 year old!
    false hy 10
    -79
    Hy
    are you comming tonight!

    JavaScript is amazing!
    
*/