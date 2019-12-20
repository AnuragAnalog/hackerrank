#include<iostream>
using namespace std;

int main()
{
    int A,B,i,j,a[1000][1000],m,n,f=0,k=0;
    cin>>m;
        for(i=0;i<m;i++) 
        {
            for(j=0;j<m;j++)
                cin>>a[i][j];
        }
        for(i=0;i<m;i++) 
        {
            f=f+a[i][i];
            k=k+a[i][m-1-i];
        }
    if(f > k)
    cout<<f-k;
    else 
    cout<<k-f;
}
