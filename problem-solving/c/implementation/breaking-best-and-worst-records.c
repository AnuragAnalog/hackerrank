#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int        i, n, cur_score, max_score, min_score, best = 0, worst = 0;

    scanf("%d", &n);

    scanf("%d", &max_score);
    min_score = max_score;

    for (i = 1; i < n; i++)
    {
        scanf("%d", &cur_score);
        if (max_score < cur_score)
        {
            best = best + 1;
            max_score = cur_score;
        }
        else if (min_score > cur_score)
        {
            worst = worst + 1;
            min_score = cur_score;
        }
    }

    printf("%d %d\n", best, worst);
    exit(0);
}
