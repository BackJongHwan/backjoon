#include<iostream>
using namespace std;

int main()
{
    int n, m;
    cin>>n >> m;
    int *basket = new int[n];
    //Initialize baskets
    for(int i = 0; i< n; i++)
    {
        basket[i] = i + 1;
    }

    for(int i = 0; i < m; i++)
    {
        int left, right;
        cin >>left >> right;
        int *temp = new int[right - left + 1];

        int j = 0;
        for(int i = left -1; i < right; i++)
        {
            temp[j] = basket[i];
            j++;
        }

        j = 0;
        for(int i = right - 1; i > left - 2 ; i--){
            basket[i] = temp[j];
            j++;
        }

       delete[] temp;
        
    }
    for(int i = 0; i< n; i++)
    {
        cout<<basket[i] << " ";
    }



    delete []basket;
    return 0;
}
