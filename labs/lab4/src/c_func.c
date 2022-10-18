#include <stdio.h>

int ADD (int num_1, int num_2) {
    printf("[C] ADD function running...\n");
    printf("[C] num_1 = %d\n", num_1);
    printf("[C] num_2 = %d\n", num_2);

    int result = num_1 + num_2;
    printf("[C] result = %d\n", result);
    return result;
}

void SUB (int num_1, int num_2, int *result) {
    // TODO: Complete the code
}
