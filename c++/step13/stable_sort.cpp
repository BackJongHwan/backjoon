#include<iostream>
#include<algorithm>
using namespace std;

class Member{
    public:
        int age;
        string name;
        int assign;
};

bool compare(const Member& member1, const Member& member2)
{
    if(member1.age == member2.age)
        return member1.assign < member2.assign;
    else return member1.age < member2.age; 
}

int main()
{
    int n;
    int sign = 0;
    cin >> n;
    Member *backjoon = new  Member[3];
    for(int i = 0; i < n; i++)
    {
        cin >> backjoon[i].age >> backjoon[i].name;
        backjoon[i].assign = sign++;
    }

    sort(backjoon, backjoon + n, compare);

    for(int i = 0; i < n; i++)
        cout<<backjoon[i].age << " "<<backjoon[i].name<<'\n';


    return 0;
}
