#include <stdio.h>

int main() {
    int i, j;

    for (i = 2; i <= 12; i++) {
        printf("sodkon %d\n", i);
        for (j = 1; j <= 12; j++) {
            printf("%d x %d = %d\n", i, j, i * j);
        }
        printf("\n");
    }

    return 0;
}
