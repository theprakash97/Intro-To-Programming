
function main(){

    // Arithmetic operators 
    let a = 3;
    let b = 7;
    let sum = a + b; console.log(sum);
    let sub = a - b; console.log(sub);
    let mul = a * b; console.log(mul);
    let div = a / b; console.log(div);
    let rem = a % b; console.log(rem);

    console.log();

    // Special operations of arithmetic 
    let x = 4;
    let y = 7;
    console.log(x / y);
    console.log(x % 2.7);

    console.log();

    // <<< Unary operators 

    // unary_plus
    let c = 4;
    let d = +c;
    console.log(d);

    // unary_minus
    let e = 4;
    let f = -e;
    console.log(f);

    // postfix 
    console.log(e++);
    console.log(e);

    // prefix 
    console.log(++e);
    console.log(e);

    console.log();

    // <<< Relational operators
    const selling_price = 23;
    const cost_price = 10;

    console.log(selling_price > cost_price);
    console.log(selling_price >= cost_price);
    console.log(selling_price < cost_price);
    console.log(selling_price <= cost_price);
    console.log(selling_price === cost_price);
    console.log(selling_price !== cost_price );

    console.log();

    // <<< Logical operators
    let user_name = "sofia";
    const password = "495/-(tymZ";

    console.log(user_name === "sofia" && password === "495/-(tymZ");
    console.log(user_name === "sofia" || password === "495-(tymz");
    console.log(!(user_name === "sofia"));

    console.log();

    // <<< Assignment operators

    let num_vl = 9;
    num_vl += 1; console.log(num_vl);
    num_vl -= 3; console.log(num_vl);
    num_vl *= 4; console.log(num_vl);
    num_vl /= 3; console.log(num_vl);
    num_vl %= 4; console.log(num_vl);

    console.log();

    // <<< Bitwise operators 

    // <<< Other operators 

    // typeof()
    console.log(typeof(45.5));

    // instanceof
    console.log("hy" instanceof String);

    return;
}
main();

/*
    ouput
    ------
    10
    -4
    21
    0.42857142857142855
    3

    0.5714285714285714
    1.2999999999999998

    4
    -4
    4
    5
    6
    6

    true
    true
    false
    false
    false
    true

    true
    true
    false

    10
    7
    28
    9.333333333333334
    1.333333333333334

    number
    false

*/