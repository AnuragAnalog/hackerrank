/*
problem statement-
              write c++ program for sparse matrix realization and operation on it transpose,fast transpose, addition of two matrices.
*/
              
              
              
#include<iostream>
using namespace std;
class matrix
{
    
    public:
        int r,c,i,j,k,nt,m[10][10],sm[10][10],sm1[10][10],sm2[10][10];
        
        void get()
        {
            cout<<"\n enter number of rows = ";
            cin>>r;
            cout<<"\n enter number of columns = ";
            cin>>c;
            cout<<"\n enter number of non zero elements = ";
            cin>>nt;
                        
            for(i=1;i<=nt;i++)
            {
                cout<<"\n enter elememts in format (row,column,non-zero value) = \n";
                cin>>sm[i][0]>>sm[i][1]>>sm[i][2];
            }
        }
        
        void display()
        {    
            sm[0][0]=r;
            sm[0][1]=c;
            sm[0][2]=nt;
            
                cout<<"elements of array = ";                    
                for(i=0;i<=nt;i++)
                {
                    for(j=0;j<3;j++)
                    {                
                    cout<<"\t"<<sm[i][j]<<"\t\t";
                    }
                cout<<"\t\n\t\t";
                }                                                                                 
            }
        
        void transpose()
        {
        
        
        sm1[0][0]=c;
        sm1[0][1]=r;
        sm1[0][2]=nt;
        k=1;
        
        for(i=0;i<c;i++)
         {
            for(j=1;j<=nt;j++)
             {
                 if(sm[j][1]==i)
                  {
                      sm1[k][0]=sm[j][1];
                      sm1[k][1]=sm[j][0];
                      sm1[k][2]=sm[j][2];
                      k++;
                  }
             }
         }
         
         cout<<"\n simple transpose is = ";
         for(i=0;i<=nt;i++)
             {
               cout<<"\n";
                for(j=0;j<3;j++)
                    {             
                     cout<<"\t"<<sm1[i][j]<<"\t"<<"\t";              
                  }
             cout<<"\t\n";     
              } 
                      
        }  
          			void fasttrans()  
          			{
          			   int f[5][5];
          			   int i,j,k;
          			   int count[6],pos[6];
          			   r=sm[0][0];
          			   c=sm[0][1];
          			   nt=sm[0][2];
          			for(i=0;i<nt;i++)
          			{
          			  count[sm[i][1]]++;
          			  }
          			  
          			  pos[0]=1;
          			  for(i=1;i<c;i++)
          			{
          			   pos[i]=pos[i-1]+count[i-1];
          			   }
          			   
          			  for(i=1;i<=nt;i++)
          			  {
          			  
          			  j=pos[sm[i][1]];
          			  f[j][0]=sm[i][1];
          			  f[j][1]=sm[i][0];
          			  f[j][2]=sm[i][2];
          			  pos[sm[i][1]]++;
          			  }
          			  cout<<"\n\tFast Transpose is\n";
          			  for(i=0;i<=nt;i++)
          			  {
          			   cout<<"\n";
          			   for(j=0;j<3;j++)
          			   {
          			   cout<<"\t"<<f[i][j];
          			   }
          			   cout<<"\n";
          			   }
          			   }
          			      
            
            
        };
        
int main()        
{
    matrix m;
    m.get();
    m.display();
    m.transpose();
    m.fasttrans();
    return 0;
}
/*
 enter number of rows = 4

 enter number of columns = 3

 enter number of non zero elements = 2

 enter elememts in format (row,column,non-zero value) = 
1
2
1

 enter elememts in format (row,column,non-zero value) = 
1
4
4
elements of array = 	4			3			2	
			1			2			1	
			1			4			4	
		
 simple transpose is = 
	3			4			2			

	2			1			1			

	-1056612432			32766			1684839728	



 */     
