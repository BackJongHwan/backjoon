#include<iostream>
using namespace std;
#define swap(a, b) {int tmp=a; a=b; b=tmp;}
int main()
{
    int n, k;
    cin >> n >> k;
    int *score = new int[n];
    for(int i = 0; i < n; i++)
        cin >> score[i];

    for(int i = 0; i < n - 1; i++)
    {
        for(int j = i; j < n; j++)
        {
            if(score[i] < score[j]){
                swap(score[i], score[j]);
            }

        }
    }
    cout<<score[k - 1]<<endl;
    
    delete []score;
    return 0;
}
