#include<iostream>
using namespace std;
int main()
{
    long long int a[5],i,min,max,f=0;
    for(i=0;i<5;i++)
    cin>>a[i];
    min=max=a[0];
    for(i=0;i<5;i++)
    {
        f=f+a[i];
        if(a[i]<min)
        min=a[i];
        else if (a[i]>max)
        max=a[i];
    }
    cout<<f-max<<" ";
    cout<<f-min;
}
