//
//  segregate0sand1s.cpp
//  
//
//  Created by Abigayle Peterson on 11/19/18.
//

#include "segregate0sand1s.hpp"
#include <iostream>

using namespace std;

void segregate0sand1(int arr[], int n) {
    int count = 0; // counts the number of 0's in the array
    
    // Loops through the arr looking for 0's and adding the total to int count
    for(int i = 0; i < n; i++) { // loop through n -> the length of the array
        if(arr[i] == 0) {
            count++;
        }
    }
    
    // Loop fills the arry with 0 until count
    for(int i = 0; i < count; i++) {
        arr[i] = 0;
    }
    
    // Loop fills remaining arr space with 1
    for(int i = count; i < n; i++) {
        arr[i] = 1;
    }
}

void print(int arr[], int n) {
    cout << "Array after segregation is " << endl;
    
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
}

int main() {
    int myArr[] = {0, 1, 0, 0, 1, 1, 0, 0, 1};
    int sizeOfArr = sizeof(myArr) / sizeof(myArr[0]);
    
    segregate0sand1(myArr, sizeOfArr);
    print(myArr, sizeOfArr);
}
