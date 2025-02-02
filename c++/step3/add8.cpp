
#include<iostream>
using namespace std;

int main()
{
    int test, a, b;
    cin >> test;
    for(int i = 0; i < test; i++)
    {
        cin >> a >> b;
        cout <<"Case #"<<i+1 << ": "<< a << " + " << b  << " = "<<  a + b<<endl;
    }
    return 0;

}
