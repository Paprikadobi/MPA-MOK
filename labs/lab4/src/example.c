#include <stdio.h>

int add(int num_1, int num_2) {
    printf("[C] add function running ...\n");
    printf("[C] num_1 = %d\n", num_1);
    printf("[C] num_2 = %d\n", num_2);

    int sum = num_1 + num_2;

    printf("[C] sum = %d\n", sum);

    return sum;
}
