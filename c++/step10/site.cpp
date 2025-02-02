#include<iostream>

using namespace std;

int main()
{
    int test;
    int min_x, max_x, min_y, max_y;
    cin >> test;
    for(int i = 0; i < test; i++)
    {
        int x, y;
        cin >> x >> y;
        if(i == 0)
        {
            min_x = x;
            max_x = x;
            min_y = y;
            max_y = y;
        }
        else{
            if(x < min_x)
                min_x = x;
            if(x > max_x)
                max_x = x;
            if(y < min_y)
                min_y = y;
            if(y > max_y)
                max_y = y;
        }

    }
    int area;
    area = (max_x - min_x) * (max_y - min_y);
    cout << area <<endl;
}
