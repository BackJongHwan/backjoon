#include<iostream>

using namespace std;

int main()
{
    int a, b, c;
    int total;
    cin >> a >> b;
    cin >> c;
    total = a * 60 + b + c;
    total = total % (60 * 24);
    a = total / 60;
    b  = total % 60;

    cout << a <<" "<< b << endl;

    return 0;

}
