#include<iostream>
#include<algorithm>
using namespace std;
int num_five(int );
int num_two(int );
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);  
    int n, m;
    cin >>n >> m;
    int two = 0;
    int five = 0;
    five += num_five(n);
    five -= num_five(m);
    five -= num_five(n - m);
    two += num_two(n);
    two -= num_two(m);
    two -= num_two(n - m);
    cout<<min(five, two)<<'\n';
    return 0;
}

int num_five(int n)
{
    int two = 0;
    while(n != 0)
    {
        two += (n /= 2);
    }
    return two;
}

int num_two(int n)
{
    int five = 0;
    while(n != 0)
    {
        five += (n /= 5);
    }

    return five;

}