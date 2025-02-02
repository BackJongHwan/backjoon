#include<iostream>
#include<string>

using namespace std;


int sum_num(int num)
{
    int sum = num;
    string str = to_string(num);
    for(int i = 0; i < str.length(); i++)
    {
        sum += int(str[i]) - int('0');
    }

    return sum;
}





int main()
{
    int n;
    cin >> n;
    int min = 0;
    int sum = 0;
    for(int i = 1; i < n + 1; i++){
        sum = sum_num(i);
        if(sum == n)
        {
            min = i;
            break;
        }
    }
    cout<<min<<endl;
    return 0;
}

