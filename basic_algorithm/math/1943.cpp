#include<iostream>
using namespace std;

int main()
{
    int n;
    int a, b;
    int max;
    int min;
    cin >> n;
    for(int i = 0 ; i < n; i++)
    {
        cin >> a >> b;
        max = 0;
        min = 0;
        for(int j = 1; j < 45001; j++)
        {
            if(a % j == 0 && b % j == 0)
            {
                if(min < j)
                    min = j;
            }
        }
        max = a * (b / min);
        cout << max <<endl;
    }
    return 0;
}
