#include <stdio.h>
#include <stdlib.h>

#define   INFINITY        1000000000

int main(void)
{
    int             i, n = 5;
    long long int   tmp, min = INFINITY, max = 0, sum = 0;

    for (i = 0; i < n; i++)
    {
        scanf("%d", &tmp);
        if (tmp > max)
        {
            max = tmp;
        }
        
        if (tmp < min)
        {
            min = tmp;
        }
        sum = sum + tmp;
    }

    printf("%lld %lld\n", sum-max, sum-min);
    exit(0);
}
