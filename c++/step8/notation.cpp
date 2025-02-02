#include<iostream>
#include<string>
#include<cmath>

using namespace std;

int main()
{
    int decimal = 0, b;
    string n;
    cin >> n >> b;

    for(int i = 0; i < n.length(); i++)
    {
        if(isalpha(n[n.length() - 1 - i]))
            decimal += (n[n.length() - 1 - i] - 55) * (pow(b, i));
        else
            decimal += (n[n.length() - 1 - i] - '0') * (pow(b, i));

    }

    cout<<decimal<<endl;

}
