#include <iostream>

using namespace std;

int main() {
    int age;
    cin >> age;

    int years = age/365;
    int months = (age % 365)/30;
    int days = age - months*30 - years*365;
    cout << years << " ano(s)" << endl;
    cout << months << " mes(es)" << endl;
    cout << days << " dia(s)" << endl;

    return 0;
}