#include<iostream>
#include<algorithm>
using namespace std;

class Member{
    public:
        int age;
        string name;
};

bool cmp(const Member &member1, const Member &member2){
    if(member1.age < member2.age)
        return true;
    else return false;

}

int main()
{
    int n;
    cin >> n;
    Member *backjoon = new  Member[n];
    for(int i = 0; i < n; i++)
    {
        cin >> backjoon[i].age >> backjoon[i].name;
    }

    stable_sort(backjoon, backjoon + n, cmp);

    for(int i = 0; i < n; i++)
        cout<<backjoon[i].age << " "<<backjoon[i].name<<'\n';

    delete[]backjoon;
    
    return 0;
}
