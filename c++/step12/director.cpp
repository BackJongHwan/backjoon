#include<iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int num_end = 665;
    int index = 0;
    while(true)
    {
        num_end++;
        string end = to_string(num_end);
        bool consecutive = false;
        for(int i = 0; i < end.length() - 2; i++)
        {
            if(end[i] == '6' && end[i + 1] == '6' && end[i + 2] == '6')
                consecutive = true;
        }
        if(consecutive) index++;
        if(n == index)
            break;
    }

    cout<<num_end<<endl;
}
