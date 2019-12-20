#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int        i, n, bill_charge = 0, bill_actual, price, k;

    scanf("%d %d", &n, &k);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &price);
        if (i == k)
        {
            continue;
        }
        bill_charge += price;
    }
    scanf("%d", &bill_actual);

    if (bill_actual == bill_charge/2)
    {
        printf("Bon Appetit\n");
    }
    else
    {
        printf("%d\n", bill_actual-bill_charge/2);
    }

    exit(0);
}
