#include <stdio.h>
#include <stdlib.h>

#define MAX        100000

int main(void)
{
    int        i, m, n, a, b, s, t, apple = 0, orange = 0, d;

    scanf("%d %d", &s, &t);
    scanf("%d %d", &a, &b);
    scanf("%d %d", &m, &n);

    for (i = 0; i < m; i++)
    {
        scanf("%d", &d);
        if (a + d >= s && a + d <= t)
        {
            apple = apple + 1;
        }
    }

    for (i = 0; i < n; i++)
    {
        scanf("%d", &d);
        if (b + d >= s && b + d <= t)
        {
            orange = orange + 1;
        }
    }

    printf("%d\n%d\n", apple, orange);
    exit(0);
}
