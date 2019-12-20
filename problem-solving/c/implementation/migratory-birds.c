#include <stdio.h>
#include <stdlib.h>

#define MAX        5

int main(void)
{
    int        i, maxi, type, type_arr[MAX], n;

    for (i = 0; i < MAX; i++)
    {
        type_arr[i] = 0;
    }

    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &type);
        type_arr[type-1] += 1;
    }

    maxi = max_with_key(type_arr, MAX);
    printf("%d\n", maxi);

    exit(0);
}

int max_with_key(int arr[], int n)
{
    int        i, key, max = 0;

    for (i = 0; i < n; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
            key = i;
        }
    }

    return key+1;
}
