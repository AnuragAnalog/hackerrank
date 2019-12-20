#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int        year;

    scanf("%d", &year);

    if (year == 1918)
    {
        printf("26.09.1918\n");
        exit(0);
    }

    if ((year < 1918 && year%4 == 0) || (year > 1918 && ((year%4 == 0 && year%100 != 0) || year%400 == 0)))
    {
        printf("12.09.%d\n", year);
    }
    else
    {
        printf("13.09.%d\n", year);
    }

    exit(0);
}

