#include <stdbool.h>
#define STB_DS_IMPLEMENTATION
#include "stb_ds.h"
#include "utils.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char test_input[] = "7 6 4 2 1\n"
                    "1 2 7 8 9\n"
                    "9 7 6 2 1\n"
                    "1 3 2 4 5\n"
                    "8 6 4 4 1\n"
                    "1 3 6 7 9\n";

bool is_valid(const int *levels) {
        int increasing = (levels[1] > levels[0]) ? 1 : -1;
        for (int i = 1; i < arrlen(levels); i++) {
                int previous = levels[i - 1];
                int current = levels[i];
                int direction = (current > previous) ? 1 : -1;

                // No direction is unsafe
                if (current == previous) {
                        return false;
                }

                // Wrong direction
                if (direction != increasing)
                        return false;

                // Too high jump
                if (abs(previous - current) > 3)
                        return false;
        }

        return true;
}
void part1(const char *input) {
        char *owned_input = strdup(input);
        int safe_reports = 0;

        char **lines = split_str(owned_input, "\n");
        foreach (char *, line, lines) {
                char **levels_str = split_str(*line, " ");

                int *levels = NULL;
                foreach (char *, level, levels_str) {
                        arrput(levels, atoi(*level));
                }

                if (is_valid(levels)) {
                        safe_reports++;
                }

                arrfree(levels);
        }

        printf("%d\n", safe_reports);
        free(owned_input);
}

void part2(const char *input) {
        char *owned_input = strdup(input);
        int safe_reports = 0;

        char **lines = split_str(owned_input, "\n");
        foreach (char *, line, lines) {
                char **levels_str = split_str(*line, " ");

                int *levels = NULL;
                foreach (char *, level, levels_str) {
                        arrput(levels, atoi(*level));
                }

                // Remove one level and try, no need to check non-dampened
                for (int i = 0; i < arrlen(levels); i++) {
                        int *adj_arr = NULL;
                        for (int j = 0; j < arrlen(levels); j++) {
                                if (i != j)
                                        arrput(adj_arr, levels[j]);
                        }
                        bool valid = is_valid(adj_arr);
                        arrfree(adj_arr);
                        if (valid) {
                                safe_reports++;
                                break;
                        }
                }
                arrfree(levels);
        }

        printf("%d\n", safe_reports);
        free(owned_input);
}

int main() {
        char *input = read_stdin();
        // part1(test_input);
        part1(input);
        // part2(test_input);
        part2(input);
        return 0;
}
