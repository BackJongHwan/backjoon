#include<iostream>
using namespace std;

bool prime(int n)
{
    for(int i = 2; i < (n / 2); i++)
    {
        if(n % i == 0) return false;
    }
    return true;
}

void goldbach(int n)
{
    int a, b;
    a = 3;
    b = n - a;
    while(true)
    {
        if(prime(a) && prime(b)) break;
        else{
            a +=2; b -= 2;
        }
    }
    cout << n <<" = "<< a <<" + " << b << '\n';
}

int main()
{
    int n;
    while(true)
    {
        cin >> n;
        if(n == 0) break;
        else{
            goldbach(n);
        }
    }
    return 0;
}