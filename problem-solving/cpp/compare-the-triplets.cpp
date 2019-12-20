#include<iostream>
using namespace std;
int main()
{
    int a[3],b[3],i,j=0,k=0;

    for(i=0;i<3;i++)
    cin>>a[i];

    for(i=0;i<3;i++)
    cin>>b[i];

    for(i=0;i<3;i++)
    {
        if(a[i]>b[i])
        j=j+1;
        else if(a[i]<b[i])
        k=k+1;
    }
    cout<<j<<" "<<k;

}
