#define STB_DS_IMPLEMENTATION
#include "stb_ds.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utils.h"

char test_input[] = "47|53\n"
                    "97|13\n"
                    "97|61\n"
                    "97|47\n"
                    "75|29\n"
                    "61|13\n"
                    "75|53\n"
                    "29|13\n"
                    "97|29\n"
                    "53|29\n"
                    "61|53\n"
                    "97|53\n"
                    "61|29\n"
                    "47|13\n"
                    "75|47\n"
                    "97|75\n"
                    "47|61\n"
                    "75|61\n"
                    "47|29\n"
                    "75|13\n"
                    "53|13\n"
                    "\n"
                    "75,47,61,53,29\n"
                    "97,61,53,29,13\n"
                    "75,29,13\n"
                    "75,97,47,61,53\n"
                    "61,13,29\n";

typedef struct {
        int key;
        int value;
} SetItem;

void part1(const char *input) {
        char *first_part_end = strstr(input, "\n\n");
        char *first = strndup(input, first_part_end - input);
        struct {
                int key;
                SetItem *value; // int array
        } *lookup = NULL;

        int a, b;
        while (sscanf(first, "%d|%d\n", &a, &b) == 2) {
                SetItem *found = hmget(lookup, a);
                hmput(found, b, 0);
                hmput(lookup, a, found);
                first = strchr(first, '\n');
                if (first)
                        first++;
                else
                        break;
        }
        free(first);


        int sum = 0;
        char *second = strndup(first_part_end + 2, strlen(first_part_end + 2));
        char *rest = NULL;
        char *line; // rest
        for (line = strtok_r(second, "\n", &rest); line != NULL;
             line = strtok_r(NULL, "\n", &rest)) {
                int *pages = NULL;
                char *rest2 = NULL;
                char *token;
                for (token = strtok_r(line, ",", &rest2); token != NULL;
                     token = strtok_r(NULL, ",", &rest2)) {
                        arrput(pages, atoi(token));
                }

                bool valid_order = true;
                for (int i = 0; i < arrlen(pages); i++) {
                        SetItem *rules = hmget(lookup, pages[i]);
                        for (int j = i + 1; j < arrlen(pages); j++) {
                                if (hmgeti(rules, pages[j]) < 0) {
                                        valid_order = false;
                                        goto done; // YOLO
                                }
                        }
                }
        done:

                if (valid_order) {
                        int len = arrlen(pages);
                        sum += pages[len/2];
                }

                arrfree(pages);
        }
        printf("%d", sum);

        // Free the lookup table
        for (int i = 0; i < hmlen(lookup); i++) {
                hmfree(lookup[i].value);
        }
        hmfree(lookup);
        free(first);
        free(second);
}

int main() {
        char *input = read_stdin();
        part1(input);
        return 0;
}
