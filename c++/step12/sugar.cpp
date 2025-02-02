#include<iostream>
using namespace std;
int main()
{
    int n;
    int min;
    bool exist = false;
    int kg_5, kg_3 ;
    cin >> n;
    kg_5 = n / 5;
    kg_3 = n / 3;
    for(int i = 0; i < kg_5 + 1; i++)
        for(int j = 0; j < kg_3 + 1; j++)
            if(5 * i + j * 3 == n)
            {
                if(!exist) min = i + j;
                else{
                    if(i + j <min)
                        min = i + j;
                }
                exist = true;
            }
    if(!exist) min = -1;
    cout<<min<<endl;
    return 0;
}

