#include<iostream>
#include<string>
using namespace std;

int main()
{
    int decimal, b, remain;
    string str;
    string temp;
    cin >> decimal >> b;
    while(true){
        if(decimal == 0)
            break;
        remain = decimal % b;
        decimal /= b;
        if(remain > 9)
           temp = char(remain + 55); 
        else
            temp = char(remain + '0');
        str.insert(0, temp);

    }
    cout<<str<<endl;

}
