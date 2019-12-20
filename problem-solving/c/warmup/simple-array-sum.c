#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int arr, i, n, sum=0;

    scanf("%d", &n);

    for(i=0;i<n;i++)
    {
        scanf("%d", &arr);
        sum=sum + arr;
    }

    printf("%d\n",sum);
    exit(0);
}
