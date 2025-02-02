#include<iostream>
using namespace std;

int main()
{
    int m, n;
    cin >>m >> n;
    int prime = 0, sum = 0;
    int min;
    int factor;
    for(int i = m; i < n + 1; i++)
    {
        if(i > 1)
        {
            for(factor = 2; factor < i; factor++)
            {
               if(i % factor == 0)
                   break;
            }
            if(factor == i){
                sum += factor;
                if(prime == 0)
                    min = factor;
                prime++;
            }
        }
    }
    if(prime != 0)
        cout<<sum<<'\n'<<min<<endl;
    else
        cout<<-1<<endl;
}
