#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int d1, d2,d3;
    int reward;
    cin >> d1 >> d2 >> d3;
    if(d1 == d2 && d1 == d3)
    {   
       reward = 10000 + d1 * 1000; 
    }
    else if(d1 == d2 || d1 == d3)
    {
        reward = 1000 + d1 * 100;
    }
    else if(d2 == d3)
    {
        reward = 1000 + d2 * 100;
    }
    else{
        reward = 100 * max({d1, d2, d3});
    }
    cout<<reward<<endl;
    
}
