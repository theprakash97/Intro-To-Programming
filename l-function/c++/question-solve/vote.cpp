#include <iostream>
using namespace std;

// Given the age of a person, write a function to check if the person is eligible to vote or not.

bool checkEligible(int age, int limit){
    if(age >= limit){
        // the person is eligible
        return true;
    }else{
        // the person is not eligible
        return false;
    }
}

int main(){
    int voting_limit = 18;
    int is_eligible_for_voting = checkEligible(15,voting_limit);
    if(is_eligible_for_voting){
        cout << "Yes, the current person is eligible to vote" << endl;
    }else{
        cout << "No, the current person is not eligibel to vote" << endl;
    }
    return 0;
}
/*
    output
    -------
    No, the current person is not eligibel to vote
    
*/