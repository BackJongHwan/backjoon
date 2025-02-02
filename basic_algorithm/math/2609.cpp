#include<iostream>
using namespace std;
int main()
{
    int a, b;
    int min = 0;
    int max;
    cin >> a >> b;
    for(int i = 1; i < 10001; i++)
    {
        if(a % i == 0 && b % i == 0)
        {
            if(min < i)
                min = i;
        }
    }
    cout<<min<<endl;
    max = a * (b / min);
    cout<<max<<endl;

    return 0;
}