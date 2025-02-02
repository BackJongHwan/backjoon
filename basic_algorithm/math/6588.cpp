#include<iostream>
using namespace std;

#define MAX_SIZE 1000000
void make_prime(int prime[])
{
    int check = 2;
    for(int i = 0; i < MAX_SIZE + 1; i++)
    {
        prime[i] = 1;
    }
    while(check < MAX_SIZE + 1)
    {
        if(prime[check] == 1)
        {
            int j = 2;
            while(check * j < MAX_SIZE + 1)
            {
                prime[check * j ]=0;
                j++;
            }
        }
        check++;
    }
}
void goldbach(int prime[], int n)
{
    int a = 3; int b = n - a;
    int check = 0;
    while(a <= b)
    {
        if(prime[a] == 1 & prime[b] == 1){
            check = 1;
            break;
        } 
        else{
            a+=2; b -=2;
        }
    }
    if(check)
    {
        cout<<n<<" = "<<a<<" + "<<b<<'\n';
    }else{
        cout<<"Goldbach's conjecture is wrong."<<endl;
    }
}

int main()
{
    ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
    int n;
    int prime[MAX_SIZE + 1];
    make_prime(prime);
    while(true)
    {
        cin >> n;
        if(n == 0) break;
        else{
            goldbach(prime, n);
        }
    }
    return 0;
}