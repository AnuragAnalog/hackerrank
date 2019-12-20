#include<iostream>
using namespace std;

int main()
{
    int n,i,j,k;
    cin>>n;
    for(k=0;k<n;k++)
    {
    for(i=n-k-2;i>=0;i--)
    {
        cout<<" ";
    }
    for(j=0;j<k+1;j++)
    {    
        cout<<"#";
    }
    cout<<"\n";
    }
}
