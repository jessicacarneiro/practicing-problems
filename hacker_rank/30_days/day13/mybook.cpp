#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

class MyBook : public Book {
    protected:
        double price;
    public:
        MyBook(string t,string a, double p): Book(t,a) {
            price=p;
        }
        void display() {
            cout << "Title: " << this->title << endl << "Author: " << this->author << endl << "Price: " << this->price << endl;
        }

};