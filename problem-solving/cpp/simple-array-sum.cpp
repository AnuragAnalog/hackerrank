#include<iostream>
using namespace std;

int main()
{
    int a,b[1001],i,f=0;
    
    cin>>a;
    for(i=0;i<a;i++)
    cin>>b[i];
    
    for(i=0;i<a;i++)
    f=f+b[i];
    cout<<f;
    
    return 0;
}
