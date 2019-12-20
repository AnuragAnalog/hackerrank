#include <stdio.h>
#include <stdlib.h>

#define   MAX       1000

int absol(int a, int b);

int main(void)
{
    int        i, j, n, arr[MAX][MAX], front = 0, back = 0,absval;

    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }

    for (i = 0; i <  n; i++)
    {
        front = front + arr[i][i];
        back = back + arr[n-1-i][i];
    }

    absval = absol(front, back);
    printf("%d\n", absval);
    exit(0);
}

int absol(int a, int b)
{
    if (a - b > 0)
    {
        return a - b;
    }
    else
    {
        return b - a;
    }
}
