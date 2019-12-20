#include <stdio.h>
#include <stdlib.h>

#define   MAX       3

int main(void)
{
    int a[MAX], b[MAX], as = 0, bs = 0, i;

    for(i = 0; i < MAX; i++)
    {
        scanf("%d",&a[i]);
    }
    
    for(i = 0;i < MAX; i++)
    {
        scanf("%d",&b[i]);
    }

    for(i = 0; i < MAX; i++)
    {
        if(a[i] < b[i])
        bs++;
        else if(a[i] > b[i])
        as++;
    }

    printf("%d %d\n",as,bs);
    exit(0);
}
