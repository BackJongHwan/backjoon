#include<iostream>

using namespace std;

int main()
{
    long int n, length;
    cin >> n;
    int number = 1;
    int room = 1;
    int a = 1;
    length = 1;
    while(n > number)
    {
        number = 1 + 6 * room;
        a++;
        room += a;
        length++;
        //cout<<"a: "<<a<<" room: "<<room<<"length: "<<length<<endl;
    }

    cout<<length<<endl;
    
}
