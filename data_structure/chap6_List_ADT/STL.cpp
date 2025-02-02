#include<cstdlib>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    int a[] = {17, 12, 33, 15, 62, 45};
    vector<int> v(a, a +6);
    vector<int>::iterator it;
    cout<<v.size()<<endl; //6
    v.pop_back(); //45 delete
    cout<<v.size()<<endl; //5
    v.push_back(19); //19 append
    cout<<v.front()<<" "<<v.back()<<endl;
    sort(v.begin(), v.begin() + 4);//{12, 15, 17, 33, 62, 19};
    for(it = v.begin(); it != v.end(); ++it)
        cout<<*it<<" ";
    cout<<endl;
    v.erase(v.end() - 4, v.end() - 2);//{12, 15, 62, 19};
    for(it = v.begin(); it != v.end(); ++it)
        cout<<*it<<" ";
    cout<<endl;
    cout<<v.size()<<endl;//4

    char b[] = {'b', 'r', 'a', 'v', 'o'};
    vector<char> w(b, b + 5);
    random_shuffle(w.begin(), w.end());
    w.insert(w.begin(), 's');

    for(vector<char>::iterator p = w.begin(); p!= w.end(); ++p)
        cout<<*p<<" ";
    cout<<endl;
    return EXIT_SUCCESS;
}