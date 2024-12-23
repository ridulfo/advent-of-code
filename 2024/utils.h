#pragma once
#include <time.h>

char *read_stdin();
char **split_str(const char *str, const char *substr);
void splitfree(char **arr);

#define foreach(type, item, array)                                             \
        for (type *item = (array); item < (array) + arrlen(array); item++)

#define BENCHMARK_RUNS 10
#define BENCHMARK(code_block)                                                  \
        do {                                                                   \
                double total_time = 0.0;                                       \
                for (int i = 0; i < BENCHMARK_RUNS; i++) {                     \
                        clock_t start = clock();                               \
                        code_block;                                            \
                        clock_t end = clock();                                 \
                        double time_taken =                                    \
                            ((double)(end - start)) / CLOCKS_PER_SEC;          \
                        total_time += time_taken;                              \
                }                                                              \
                printf("Average execution time: %f seconds\n",                 \
                       total_time / BENCHMARK_RUNS);                           \
        } while (0)
