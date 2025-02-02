#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    //int sqrt_n;
    int *factor = new int[n];

    for(int i = 0; i < n; i++)
    {
        factor[i] = 0;
    }
    
    //sqrt_n = int(sqrt(n));
    int th = 0;

    for(int i = 1; i < n + 1; i++)
    {
       if(n % i  == 0){
           factor[th] = i;
           th++;
       }
    }

    cout<<factor[k-1]<<endl;

    delete []factor;

    return 0;
    
}
