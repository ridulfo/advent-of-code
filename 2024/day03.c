#define STB_DS_IMPLEMENTATION
#include "stb_ds.h"
#include "utils.h"

#include <regex.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

const char test_input[] =
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
const char test_input2[] =
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";

void part1(const char *input) {
        const char *pattern = "mul\\(([0-9]+),([0-9]+)\\)";
        regex_t regexCompiled;
        regmatch_t groupArray[3];
        const char *cursor = input;

        if (regcomp(&regexCompiled, pattern, REG_EXTENDED)) {
                printf("Could not compile regular expression.\n");
                return;
        }

        int sum = 0;
        while (regexec(&regexCompiled, cursor, 3, groupArray, 0) == 0) {
                size_t full_match_len =
                    groupArray[0].rm_eo - groupArray[0].rm_so;
                char full_match[full_match_len + 1];
                strncpy(full_match, cursor + groupArray[0].rm_so,
                        full_match_len);
                full_match[full_match_len] = '\0';

                size_t group1_len = groupArray[1].rm_eo - groupArray[1].rm_so;
                char group1[group1_len + 1];
                strncpy(group1, cursor + groupArray[1].rm_so, group1_len);
                group1[group1_len] = '\0';

                size_t group2_len = groupArray[2].rm_eo - groupArray[2].rm_so;
                char group2[group2_len + 1];
                strncpy(group2, cursor + groupArray[2].rm_so, group2_len);
                group2[group2_len] = '\0';

                int a = atoi(group1);
                int b = atoi(group2);
                sum += a * b;

                cursor += groupArray[0].rm_eo;
        }
        printf("%d\n", sum);

        regfree(&regexCompiled);
}

void part2(const char *input) {
        const char *pattern = "mul\\(([0-9]+),([0-9]+)\\)|do\\(\\)|don't\\(\\)";
        regex_t regexCompiled;
        regmatch_t groupArray[3];
        const char *cursor = input;

        if (regcomp(&regexCompiled, pattern, REG_EXTENDED)) {
                printf("Could not compile regular expression.\n");
                return;
        }

        int sum = 0;
        bool enabled = true;
        while (regexec(&regexCompiled, cursor, 3, groupArray, 0) == 0) {
                size_t full_match_len =
                    groupArray[0].rm_eo - groupArray[0].rm_so;
                char full_match[full_match_len + 1];
                strncpy(full_match, cursor + groupArray[0].rm_so,
                        full_match_len);
                full_match[full_match_len] = '\0';

                if (strcmp(full_match, "do()") == 0) {
                        enabled = true;
                        cursor += groupArray[0].rm_eo;
                        continue;
                } else if (strcmp(full_match, "don't()") == 0) {
                        enabled = false;
                        cursor += groupArray[0].rm_eo;
                        continue;
                }

                if (enabled) {
                        size_t group1_len =
                            groupArray[1].rm_eo - groupArray[1].rm_so;
                        char group1[group1_len + 1];
                        strncpy(group1, cursor + groupArray[1].rm_so,
                                group1_len);
                        group1[group1_len] = '\0';

                        size_t group2_len =
                            groupArray[2].rm_eo - groupArray[2].rm_so;
                        char group2[group2_len + 1];
                        strncpy(group2, cursor + groupArray[2].rm_so,
                                group2_len);
                        group2[group2_len] = '\0';

                        int a = atoi(group1);
                        int b = atoi(group2);
                        sum += a * b;
                }

                cursor += groupArray[0].rm_eo;
        }
        printf("%d\n", sum);

        regfree(&regexCompiled);
}

int main() {
        char *input = read_stdin();
        part1(input);
        part2(input);
        return 0;
}
