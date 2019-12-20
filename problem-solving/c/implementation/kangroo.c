#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int        x1, x2, v1, v2, meet = 0;

    scanf("%d %d %d %d", &x1, &v1, &x2, &v2);

    if (x1 > x2)
    {
        while (x2 < x1)
        {
            x1 = x1 + v1;
            x2 = x2 + v2;
            if (x1 == x2)
            {
                meet = 1;
                break;
            }
        }
    }
    else if (x2 > x1)
    {
        while (x1 < x2)
        {
            x1 = x1 + v1;
            x2 = x2 + v2;
            if (x1 == x2)
            {
                meet = 1;
                break;
            }
        }
    }
    else if (x1 == x2)
    {
        meet = 1;
    }

    if (meet == 1)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }

    exit(0);
}
