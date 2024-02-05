#include<iostream>
using namespace std;
template<typename T>
T genericMin(T a, T b){
    return (a < b  ? a : b);
}

int main()
{
    cout<<genericMin(3, 4)<<' '
    << genericMin(1.1, 3.1)<<' '
    << genericMin('t', 'g')<<endl;
    return 0;
}