#include <stdio.h>
#include <stdlib.h>

#define MAX      100

int main(void)
{
    int        i, j, t, n, k, count, time;

    scanf("%d", &t);

    for (i = 0; i < t; i++)
    {
        scanf("%d %d", &n, &k);
        count = 0;

        for (j = 0; j < n; j++)
        {
            scanf("%d", &time);
            if (time <= 0)
            {
                count = count + 1;
            }
        }

        if (count >= k)
        {
            printf("NO\n");
        }
        else
        {
            printf("YES\n");
        }
    }

    exit(0);
}