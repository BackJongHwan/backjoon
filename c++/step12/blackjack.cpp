#include<iostream>
using namespace std;

int main()
{
    int n, m;
    int *card;
    cin >> n >> m;
    card = new int[n];
    for(int i = 0; i < n; i++)
    {
       cin >> card[i];
    }

    int sum = 0;
    int max = 0;

    for(int i = 0; i < n -2; i++)
        for(int j = i + 1 ; j < n - 1;j++)
            for(int k = j + 1; k < n; k++)
            {
                sum = card[i] + card[j] + card[k];
                if(sum <= m)
                {
                    if(sum > max)
                        max = sum;
                }
                sum = 0;

            }


    cout<<max<<endl;

}
