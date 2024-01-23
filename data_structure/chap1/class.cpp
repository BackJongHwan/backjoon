#include<iostream>
#include<string>
using namespace std;

class Passenger{
    public:
        Passenger();
        bool isFrequentFlyer() const;
        void makeFrequentFlyer(const string & newFreqFlyerNo);
    private:
        string name;
        MealType mealPref;
        bool isFreqFlyer;
        string freqFlyerNo;
};

bool Passenger::isFrequentFlyer() const
{
    return isFreqFlyer;
}

void Passenger::makeFrequentFlyer(const string &newFreqFlyerNo){
    isFreqFlyer = true;
    freqFlyerNo = newFreqFlyerNo;
}


