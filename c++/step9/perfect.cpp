#include<iostream>
using namespace std;

int main()
{
    int n;
    int *factor;
    int th;
    while(true){
        cin >> n;
        if(n == -1) break;
        factor = new int[n];
        for(int i = 0; i < n; i++)
        {
            factor[i] = 0;
        }
        th = 0;

        for(int i = 1; i < n; i++)
        {
           if(n % i  == 0){
               factor[th] = i;
               th++;
           }
        }
        th = 0; 
        int sum = 0;
        while(factor[th] != 0)
        {
            sum += factor[th];
            th++;
        }
        th  = 0;
        if(sum == n){
            cout<<n<<" = ";
            while(factor[th] != 0){
                if(factor[th + 1] == 0)
                    cout<<factor[th]<<endl;
                else
                    cout<<factor[th]<<" + ";

                th++;
            }
                
        }
        else
            cout<<n<<" is NOT perfect."<<endl;

    }
}
