#include<iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    float *score = new float[n];
    //Initialize scor
    for(int i = 0; i < n; i++)
    {
        cin >> score[i];
    }
    //find max
    float max = 0;
    for(int i = 0; i < n; i++)
    {
        if(score[i] > max) max = score[i];

    }

    //refactoreing score
    float sum = 0;
    for(int i = 0; i < n; i++)
    {
        score[i] = score[i]/ max * 100;
        sum += score[i];
    }

    float average = sum / n;

    cout << average<< endl;


    delete []score;
    return 0;
}
