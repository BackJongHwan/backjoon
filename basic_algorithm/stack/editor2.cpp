#include<iostream>
#include<string>
#include<deque>
using namespace std;


int main()
{
    deque<char> D_left;
    deque<char> D_right;
    string str; int n; char cmd;
    cin >> str;
    cin >> n;
    for(int i = 0; i < str.size(); i++)
    {
        D_left.push_back(str[i]);
    }

    for(int i = 0; i < n; i++)
    {
        cin >> cmd;
        if(cmd == 'L'){
            if(!D_left.empty())
            {
                D_right.push_back(D_left.back());
                D_left.pop_back();
            }
        }else if(cmd == 'D'){
            if(!D_right.empty()){
                D_left.push_back(D_right.back());
                D_right.pop_back();
            }
        }else if(cmd == 'B'){
            if(!D_left.empty())
                D_left.pop_back();
        }else if(cmd == 'P'){
            char ch;
            cin >> ch;
            D_left.push_back(ch);
        }
    }
    while(!D_left.empty())
    {
        cout<<D_left.front();
        D_left.pop_front();
    }
    while(!D_right.empty())
    {
        cout<<D_right.back();
        D_right.pop_back();
    }
    cout<<'\n';
    return 0;
}