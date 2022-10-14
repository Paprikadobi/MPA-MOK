#include <stdio.h>

void sub(int num_1, int num_2, int *result) {
    printf("[C] sub function running ...\n");
    printf("[C] num_1 = %d\n", num_1);
    printf("[C] num_2 = %d\n", num_2);

    *result = num_1 - num_2;

    printf("[C] res = %d\n", *result);
}