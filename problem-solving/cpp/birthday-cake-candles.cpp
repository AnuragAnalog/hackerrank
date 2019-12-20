#include<iostream>
using namespace std;
int main()
{
    long long int n,i,a[100000],f=0,max;
    cin>>n;
    max=a[0];
    for(i=0;i<n;i++)
    cin>>a[i];
    for(i=0;i<n;i++)
    {
        if(a[i]>max)
        max=a[i];
    }
    for(i=0;i<n;i++)
    {
        if(a[i]==max)
        f=f+1;
    }
    cout<<f;
}
