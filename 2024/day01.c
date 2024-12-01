#define STB_DS_IMPLEMENTATION
#include "stb_ds.h"
#include "utils.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char test_input[] = "3   4\n"
                    "4   3\n"
                    "2   5\n"
                    "1   3\n"
                    "3   9\n"
                    "3   3\n";

int compare_function(const void *a, const void *b) {
        int *x = (int *)a;
        int *y = (int *)b;
        return *y - *x;
}

void part1(const char *input) {
        char* owned_input = strdup(input);
        int *a = NULL, *b = NULL;

        char *rest = NULL;
        char *token;
        for (token = strtok_r(owned_input, " \n", &rest); token != NULL;
             token = strtok_r(NULL, " \n", &rest)) {
                arrput(a, atoi(token));
                token = strtok_r(NULL, " \n", &rest);
                arrput(b, atoi(token));
        }

        qsort(a, arrlen(a), sizeof(int), compare_function);
        qsort(b, arrlen(b), sizeof(int), compare_function);

        int *diffs = NULL;
        for (int i = 0; i < arrlen(a); i++) {
                arrput(diffs, abs(a[i] - b[i]));
        }

        int sum = 0;
        for (int i = 0; i < arrlen(diffs); i++) {
                sum += diffs[i];
        }

        printf("%d\n", sum);

        arrfree(a);
        arrfree(b);
        arrfree(diffs);
        free(owned_input);
}

void part2(const char *input) {
        char* owned_input = strdup(input);
        int *a = NULL, *b = NULL;

        char *rest = NULL;
        char *token;
        for (token = strtok_r(owned_input, " \n", &rest); token != NULL;
             token = strtok_r(NULL, " \n", &rest)) {
                arrput(a, atoi(token));
                token = strtok_r(NULL, " \n", &rest);
                arrput(b, atoi(token));
        }

        struct {
                int key;
                int value;
        } *lookup = NULL;
        for (int i = 0; i < arrlen(b); i++) {
                int current = b[i];
                if (hmgeti(lookup, current) == -1) {
                        int count = 0;
                        for (int j = 0; j < arrlen(b); j++) {
                                if (b[j] == current)
                                        count++;
                        }
                        hmput(lookup, current, count);
                }
        }

        int sum = 0;
        for (int i = 0; i < arrlen(a); i++) {
                int current = a[i];
                int count = hmget(lookup, current); // 0 if key not present
                sum += current * count;
        }

        printf("%d\n", sum);

        arrfree(a);
        arrfree(b);
        hmfree(lookup);
        free(owned_input);
}

int main() {
        char *input = read_stdin();
        part1(input);
        part2(input);
        return 0;
}
