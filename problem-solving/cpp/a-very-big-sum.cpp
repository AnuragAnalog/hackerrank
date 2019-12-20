#include<iostream>
using namespace std;

int main()
 {
    long int a[10],i,n,f=0;
    
    cin>>n;
    for(i=0;i<n;i++)
    cin>>a[i];
    
    for(i=0;i<n;i++)
    f=f+a[i];
    
    cout<<f;
}
