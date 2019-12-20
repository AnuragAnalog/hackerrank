#include<iostream>
using namespace std;
int main()
{
    int n,a[100],i;
    float f=0,k=0,l=0;
    cin>>n;
    for(i=0;i<n;i++)
    cin>>a[i];
    for(i=0;i<n;i++)
    {
        if(a[i]>0)
        f=f+1;
        else if(a[i]<0)
        k=k+1;
        else
        l=l+1;
    }
    cout<<f/n<<"\n";
    cout<<k/n<<"\n";
    cout<<l/n<<"\n";
}
