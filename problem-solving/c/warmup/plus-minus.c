#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int        i, tmp, pos = 0, neg = 0, zero = 0, n;

    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &tmp);
        if (tmp > 0)
        {
            pos = pos + 1;
        }
        else if (tmp < 0)
        {
            neg = neg + 1;
        }
        else if (tmp == 0)
        {
            zero = zero + 1;
        }
    }

    printf("%f\n", (float)pos/n);
    printf("%f\n", (float)neg/n);
    printf("%f\n", (float)zero/n);
    exit(0);
}
