#include<iostream>
using namespace std;

int main()
{
    int a = 1 , q = 1, p = 1;
    int x;
    cin >> x;
    while(x > a)
    {
        x -= a;
        a++;
        p++;
    }
    while(x > 1)
    {
        p--;
        q++;
        x--;
    }

    if(a % 2 == 1)
    {
        int temp = q;
        q = p;
        p = temp;
    }
    cout<<q<<"/"<<p<< endl;

}
