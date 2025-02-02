#include<iostream>
using namespace std;

int main()
{
    int angle[3];
    int sum = 0;
    for(int i = 0; i < 3; i++)
    {
        cin >> angle[i];
        sum += angle[i];
    }

    if(sum == 180)
    {
       if(angle[0] == angle[1] && angle[0] == angle[2])
           cout<<"Equilateral"<<endl;
       else if(angle[0] == angle[1] || angle[0] == angle[2] || angle[1] == angle[2])
           cout<<"Isosceles"<<endl;
       else cout<<"Scalene"<<endl;
    }
    else cout<<"Error"<<endl;


    return 0;
}
