#include <stddef.h>
#include <stdlib.h>
#define STB_DS_IMPLEMENTATION
#include "stb_ds.h"
#include "utils.h"

#include <assert.h>
#include <regex.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

const char test_input[] = "MMMSXXMASM\n"
                          "MSAMXMSMSA\n"
                          "AMXSXMAAMM\n"
                          "MSAMASMSMX\n"
                          "XMASAMXAMM\n"
                          "XXAMMXXAMA\n"
                          "SMSMSASXSS\n"
                          "SAXAMASAAA\n"
                          "MAMMMXMMMM\n"
                          "MXMXAXMASX\n";

int count_xmas(char *string) {
        int count = 0;
        char *pos = string;
        while ((pos = strstr(pos, "XMAS"))) {
                count++;
                (pos)++;
        }
        pos = string;
        while ((pos = strstr(pos, "SAMX"))) {
                count++;
                (pos)++;
        }
        return count;
}

void part1(const char *input) {
        int width = (int)(strstr(input, "\n") - input) + 1; // +1 for newline
        int height = 0;
        for (size_t i = 0; i < strlen(input); i++) {
                height += input[i] == '\n';
        }
        assert(height == width - 1);

        int count = 0;

        // Rows
        for (int h = 0; h < height; h++) {
                char *row = NULL;
                for (int w = 0; w < width - 1; w++) { // -1 for new lines
                        arrput(row, input[h * width + w]);
                }
                arrput(row, 0);
                count += count_xmas(row);
                arrfree(row);
        }

        // Columns
        for (int w = 0; w < width - 1; w++) { // -1 for new lines
                char *column = NULL;
                for (int h = 0; h < height; h++) {
                        arrput(column, input[width * h + w]);
                }
                arrput(column, 0);
                count += count_xmas(column);
                arrfree(column);
        }

        // Top-Left to Bottom-Right
        for (int diagonal = 0; diagonal < width; diagonal++) {
                char *str = NULL;
                int x = diagonal, y = 0;
                while (x < width - 1 && y < height) {
                        arrput(str, input[y * width + x]);
                        x++;
                        y++;
                }
                arrput(str, 0);
                count += count_xmas(str);
                arrfree(str);
        }
        for (int diagonal = 1; diagonal < height; diagonal++) {
                char *str = NULL;
                int x = 0, y = diagonal;
                while (x < width - 1 && y < height) {
                        arrput(str, input[y * width + x]);
                        x++;
                        y++;
                }
                arrput(str, 0);
                count += count_xmas(str);
                arrfree(str);
        }

        // Top-Right to Bottom-Left
        for (int diagonal = 0; diagonal < width - 1; diagonal++) {
                char *str = NULL;
                int x = diagonal, y = 0;
                while (x >= 0 && y < height) {
                        arrput(str, input[y * width + x]);
                        x--;
                        y++;
                }
                arrput(str, 0);
                count += count_xmas(str);
                arrfree(str);
        }
        for (int diagonal = 1; diagonal < height; diagonal++) {
                char *str = NULL;
                int x = width - 2, y = diagonal; // -2 to skip newline
                while (x >= 0 && y < height) {
                        arrput(str, input[y * width + x]);
                        x--;
                        y++;
                }
                arrput(str, 0);
                count += count_xmas(str);
                arrfree(str);
        }

        printf("%d\n", count);
}

void part2(const char *input) {
        int side = (int)(strstr(input, "\n") - input) + 1; // +1 for newline
        int count = 0;
        for (int x = 0; x < side - 3; x++) {
                for (int y = 0; y < side - 3; y++) {
                        if (((input[(y + 0) * side + (x + 0)] == 'M' &&
                              input[(y + 1) * side + (x + 1)] == 'A' &&
                              input[(y + 2) * side + (x + 2)] == 'S') ||

                             (input[(y + 0) * side + (x + 0)] == 'S' &&
                              input[(y + 1) * side + (x + 1)] == 'A' &&
                              input[(y + 2) * side + (x + 2)] == 'M')) &&

                            ((input[(y + 0) * side + (x + 2)] == 'M' &&
                              input[(y + 1) * side + (x + 1)] == 'A' &&
                              input[(y + 2) * side + (x + 0)] == 'S') ||

                             (input[(y + 0) * side + (x + 2)] == 'S' &&
                              input[(y + 1) * side + (x + 1)] == 'A' &&
                              input[(y + 2) * side + (x + 0)] == 'M'))) {
                                count++;
                        }
                }
        }
        printf("%d\n", count);
}

int main() {
        char *input = read_stdin();
        // part1(test_input);
        part1(input);
        // part2(test_input);
        part2(input);
        return 0;
}
