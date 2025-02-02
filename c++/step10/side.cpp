#include<iostream>
using namespace std;

int main()
{
    int side[3];
    while(true){
        int max, index_max;
        cin >> side[0] >> side[1] >> side[2];
        if( side[0]== 0 && side[1] == 0 && side[2] == 0)
            break;
        max = side[0];
        index_max = 0;
        if(side[1] > max)
        {
            max = side[1];
            index_max = 1;
        }
        if(side[2] > max)
        {
            max = side[2];
            index_max = 2;
        }

        int sum = 0;
        for(int i = 0; i < 3; i++)
        {
            if(i != index_max)
                sum += side[i];
        }

        if(sum <= max)
        {
            cout<<"Invalid"<<endl;
        }
        else{
            if(side[0] == side[1] && side[0] == side[2])
                cout<<"Equilateral"<<endl;
            else if(side[0] == side[1] || side[0] == side[2] || side[1] == side[2])
                cout<<"Isosceles"<<endl;
            else
                cout<<"Scalene"<<endl;
        }
    }
}
