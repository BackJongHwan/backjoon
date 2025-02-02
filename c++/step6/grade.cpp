// #include<iostream>
// #include<string>
// using namespace std;
// #define num 20

// class Subject{
//     public:
//         string subject;
//         float credit;
//         string grade;
//         void print(){
//             cout<< this->subject;
//             cout<< this->credit;
//             cout<< this->grade;
//         }
// };


// // 
// int main()
// {
//     Subject sub[num];
//     for(int i = 0; i < num; i++)
//     {
//         cin >> sub[i].subject;
//         cin >> sub[i].credit;
//         cin >> sub[i].grade;
//     }

//     float total_credit = 0;
//     float total_grade = 0;

//     for(int i =  0; i < num; i++)
//     {
//         if(sub[i].grade[0] == 'P')
//             continue;
//         if(sub[i].grade[0] == 'F'){
//             total_credit += sub[i].credit;
//             continue;
//         }

//         if(sub[i].grade[1] == '+')
//         {
//             total_grade += sub[i].credit * 0.5;
//         }

//         if(sub[i].grade[0] == 'A'){
//             total_credit += sub[i].credit;
//             total_grade += sub[i].credit * 4.0;
//         }
//         else if(sub[i].grade[0] == 'B')
//         {
//             total_credit += sub[i].credit;
//             total_grade += sub[i].credit* 3.0;
//         }
//         else if(sub[i].grade[0] == 'C')
//         {
//             total_credit += sub[i].credit;
//             total_grade += sub[i].credit* 2.0;

//         }
//         else if(sub[i].grade[0] == 'D')
//         {
//             total_credit += sub[i].credit;
//             total_grade += sub[i].credit* 1.0;

//         }
//     }


//     cout<< total_grade / total_credit << endl;
//     return 0;

// }
