#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX        10

int main(void)
{
    int        i, j, n, m, l, u, value = 0, a[MAX], b[MAX];
    bool       check;

    scanf("%d %d", &n, &m);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    for (i = 0; i < m; i++)
    {
        scanf("%d", &b[i]);
    }

    l = max(a, n);
    u = min(b, m);
    for (i = l; i < u+1; i++)
    {
        check = true;
        for (j = 0; j < n; j++)
        {
            if (i%a[j] != 0)
            {
                check = false;
                break;
            }
        }

        for (j = 0; j < m; j++)
        {
            if (b[j]%i != 0)
            {
                check = false;
                break;
            }
        }

        if (check)
        {
            value = value + 1;
        }
    }
    printf("%d\n", value);

    exit(0);
}

int max(int arr[], int n)
{
    int        i, maxi = 0;

    for (i = 0; i < n; i++)
    {
        if (maxi < arr[i])
        {
            maxi = arr[i];
        }
    }

    return maxi;
}

int min(int arr[], int n)
{
    int        i, mini = 101;

    for (i = 0; i < n; i++)
    {
        if (mini < arr[i])
        {
            mini = arr[i];
        }
    }

    return mini;
}

