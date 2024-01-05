#include<iostream>
using namespace std;

int main()
{
    int factor = 2, num;
    cin >> num;
    while(true)
    {
        if(num == 1)
            break;
        if(num % factor != 0)
            factor++;
        else{
            num /= factor;
            cout<<factor<<endl;
        }
    }
}
