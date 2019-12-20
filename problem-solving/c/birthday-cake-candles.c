#include <stdio.h>
#include <stdlib.h>

#define   MAX        100000

int main(void)
{
    int        i, tmp, n, count = 0, max = 0;

    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &tmp);
        if (tmp > max)
        {
            max = tmp;
            count = 1;
        }
        else if (tmp == max)
        {
            count = count + 1;
        }
    }

    printf("%d\n", count);
    exit(0);
}
