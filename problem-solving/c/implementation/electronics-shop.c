#include <stdio.h>
#include <stdlib.h>

#define MAX        1000

int main(void)
{
    int        i, j, max = -1, b, n, m, keyboard[MAX], driver[MAX];

    scanf("%d %d %d", &b, &n, &m);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &keyboard[i]);
    }

    for (i = 0; i < m; i++)
    {
        scanf("%d", &driver[i]);
    }

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            if (keyboard[i] + driver[j] <= b && keyboard[i] + driver[j] > max)
            {
                max = keyboard[i] + driver[j];
            }
        }
    }

    printf("%d\n", max);

    exit(0);
}
