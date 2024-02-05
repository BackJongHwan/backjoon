#include<iostream>
#include<vector>
using namespace std;

int main()
{
    vector<int> a;
    vector<int>::iterator it;
    a.push_back(3);
    a.push_back(5);
    a.push_back(7);
    for(it = a.begin(); it!=a.end(); it++)
        cout<<*it<<endl;
    return 0;
}