#include <stdio.h>
#include <stdlib.h>

#define   MAX       10

int main(void)
{
    int           i, n;
    long long int a[MAX], sum = 0;
    
    scanf("%d",&n);

    for(i = 0; i < n; i++)
    {
        scanf("%lld", &a[i]);
    }

    for(i = 0; i < n; i++)
    {
        sum = sum + a[i];
    }
    
    printf("%lld\n", sum);
    exit(0);
}
