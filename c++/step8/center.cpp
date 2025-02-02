#include<iostream>
using namespace std;

int main()
{
    int n;
    int dot = 0;
    int rectangle = 1;
    cin >> n;
    for(int i = 0; i < n ;i++)
    {
        rectangle *= 2;
    }
    dot = rectangle + 1;
    cout<<dot * dot<< endl;
    return 0;
}
