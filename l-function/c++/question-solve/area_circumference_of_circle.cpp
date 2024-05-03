#include <iostream>
using namespace std;

//  Given radius of cricle. wap to print the area and circumference of the circle
/*
    formula : 
    circumference = 2 * PI * r
    area = PI * r * r
*/

int sqaure(int x){
    return x * x;
}
double circumference(int r){
    return 2 * 3.14 * r;
}

double area(int r){
    return 3.14 * sqaure(r);
}

int main(){
    int r = 3;
    cout << area(r) << " -> " << circumference(r) << endl;
    return 0;
}