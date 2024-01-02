#include<iostream>

using namespace std;

int main()
{
    int m, n;
    int *box;
    int s, e, b;
    cin >> n;
    cin >> m;
    box = new int[n];
    for(int i = 0; i < m; i++)
    {
        cin >> s >> e >> b;
        for(int j = s - 1; j < e; j++)
        {
            box[j] = b;
        }
    }

    for(int i = 0; i < n; i++)
    {
        cout << box[i] <<" ";
    }

    return 0;
}
