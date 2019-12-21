#include <stdio.h>
#include <stdlib.h>

int distance(int a, int b);

int main(void)
{
    int        i, q, x, y, z, cat1, cat2;

    scanf("%d", &q);

    for (i = 0; i < q; i++)
    {
        scanf("%d %d %d", &x, &y, &z);
        cat1 = distance(x, z);
        cat2 = distance(y, z);

        if (cat1 > cat2)
        {
            printf("Cat B\n");
        }
        else if (cat1 < cat2)
        {
            printf("Cat A\n");
        }
        else
        {
            printf("Mouse C\n");
        }
    }

    exit(0);
}

int distance(int a, int b)
{
    if (a > b)
    {
        return a - b;
    }
    else
    {
        return b - a;
    }
}

