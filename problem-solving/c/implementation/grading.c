#include <stdio.h>
#include <stdlib.h>

#define MAX        60

int main(void)
{
    int        i, n, val, grades[MAX];

    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &grades[i]);
    }

    for (i = 0; i < n; i++)
    {
        if (grades[i] < 38)
        {
            printf("%d\n", grades[i]);
            continue;
        }

        val = (grades[i]/5 + 1)*5;
        if (val - grades[i] < 3)
        {
            printf("%d\n", val);
        }
        else
        {
            printf("%d\n", grades[i]);
        }
    }
    exit(0);
}
