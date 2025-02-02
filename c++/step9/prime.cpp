#include<iostream>
using namespace std;

int main()
{
    int test, num;
    int num_prime = 0;
    int factor;
    cin >> test;
    for(int i = 0; i < test; i++)
    {
        cin >> num;
        if(num > 1)
        {
            for(factor = 2; factor < num; factor++)
            {
               if(num % factor == 0) 
                   break;
            }
            //cout<<factor<<endl;
            if(factor == num)
                num_prime++;
        }
    }
    cout<<num_prime<<endl;
}
