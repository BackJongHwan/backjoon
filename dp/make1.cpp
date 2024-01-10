#include<iostream>

using namespace std;


int make1(int n)
{
    if(n == 1) return 0;
    if(n % 3 == 0) return (make1(n / 3) + 1);
    else if(n % 2 == 0){
        return min(make1(n /2), make1(n - 1)) + 1;
    }
    else return make1(n-1) + 1;
}


int main()
{
    int n;
    cin >> n;
    int num = 0;
    num = make1(n);
    cout << num << endl;


    return 0;
}
