
function main(){

    let sym = 'g'; 
    console.log(sym);

    // character_value to ascii_value
    let ch = 'g';
    console.log(`The ascii value of ${ch} is : ${ch.codePointAt()}`);

    // ascii_value to character_value
    let num = 103;
    console.log(`The character value of ${num} is : ${String.fromCodePoint(num)}`);

    // escape sequence character
    let a = 'P';
    let b = '\t';
    let c = '\R';
    let d = '\t';
    let e = 'A';
    let user_name = a + b + c + d + e + '\n' + "my name start with (pra + kash)";
    console.log(user_name);

    return;
}
main();

/*
    output
    ---------
    g
    The ascii value of g is : 103
    The character value of 103 is : g
    P       R       A
    my name start with (pra + kash)

*/