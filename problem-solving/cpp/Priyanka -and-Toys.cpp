#include <bits/stdc++.h>

using namespace std;


// Complete the toys function below.
int toys(vector<int> w,int n) {
int c=0,i,m;
sort(w.begin(),w.end());
m=w[0];
for(i = 0; i < n; i++)
{
    if(w[i]>m+4){
        c++;
        m=w[i];
    }
}
return c;
}

int main()
{


    int n;
    cin >> n;
     
    vector<int> w(n);

    for (int i = 0; i < n; i++) {
        
        cin>>w[i];
    }

    int result = toys(w,n);

    cout << result+1<< "\n";


    return 0;
}
