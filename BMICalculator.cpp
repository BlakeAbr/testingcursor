#include <iostream>
#include <cstdlib>
#ifdef _WIN32
#include <windows.h>
#endif

using namespace std;

int main(int argc, char** argv) {
    float weight = 0;
    float height = 0;
    float bmi = 0;

    cout << "Enter your weight in kilograms: ";
    cin >> weight;
    cout << "Enter your height in meters: ";
    cin >> height;

    bmi = weight / (height * height);   

    cout << "Your BMI is " << bmi << endl;  

    return 0;
}