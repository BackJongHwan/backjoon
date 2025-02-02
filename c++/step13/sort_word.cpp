#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool compare(string str1, string str2){
    if(str1.length() == str2.length())
        return str1 < str2;
    else return str1.length() < str2.length();

}

int main()
{
    string str;
    int n;
    cin >> n;
    vector<string> v;
    for(int i = 0; i < n;i++)
    {
        cin >> str;
        if(find(v.begin(), v.end(), str) == v.end())
            v.push_back(str);
    }

    sort(v.begin(), v.end(), compare);
    for(int i = 0; i < v.size(); i++)
        cout<<v[i]<<endl;
}
