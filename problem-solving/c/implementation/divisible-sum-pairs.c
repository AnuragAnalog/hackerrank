#include <stdio.h>
#include <stdlib.h>

#define MAX        100

int main(void)
{
    int        i, j, value, arr[MAX], n, k;

    scanf("%d %d", &n, &k);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < n; i++)
    {
        for (j = i+1; j < n; j++)
        {
            if ((arr[i]+arr[j])%k == 0)
            {
                value = value + 1;
            }
        }
    }

    printf("%d\n", value);

    exit(0);
}
