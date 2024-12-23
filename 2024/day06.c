#define STB_DS_IMPLEMENTATION
#include "stb_ds.h"

#include "utils.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char test_input[] = "....#.....\n"
                    ".........#\n"
                    "..........\n"
                    "..#.......\n"
                    ".......#..\n"
                    "..........\n"
                    ".#..^.....\n"
                    "........#.\n"
                    "#.........\n"
                    "......#...\n";

typedef enum Direction {
        UP,
        RIGHT,
        DOWN,
        LEFT,
} Direction;

int side;
void print_map(bool *map, int guard_x, int guard_y) {
        for (int i = 0; i < arrlen(map); i++) {
                if (i % side == 0) printf("\n");
                if (i % side == guard_x && i / side == guard_y)
                        printf("O");
                else
                        printf("%c", map[i] ? '#' : '.');
        }
        printf("\n");
}

#define get_cell(map, x, y) (map[(y) * side + (x)])
#define coords_to_index(x, y) ((y) * side + (x))

void part1(const char *input) {
        side = (int)(strstr(input, "\n") - input);

        bool *map = NULL;
        arrsetcap(map, side * side); // Pre-alloc

        Direction dir = UP;
        int gx, gy;
        for (unsigned long i = 0; i < strlen(input); i++) {
                char curr = input[i];
                if (curr == '\n') continue;
                arrput(map, curr == '#');
                if (curr == '^') {
                        int loc = arrlen(map) - 1; // -1 for 0 based index
                        gx = loc % side;
                        gy = loc / side;
                }
        }

        int *locations = calloc(sizeof(bool), side * side);

        bool done = false;
        while (!done) {
                locations[coords_to_index(gx, gy)] = true;

                int ngx, ngy;
        reset:
                ngx = gx;
                ngy = gy;
                switch (dir) {
                case UP:
                case DOWN:
                        ngy += (dir == DOWN ? 1 : -1);
                        break;
                case RIGHT:
                case LEFT:
                        ngx += (dir == RIGHT ? 1 : -1);
                        break;
                }
                if (get_cell(map, ngx, ngy)) { // if obstruction
                        dir = (dir + 1) % 4;
                        goto reset; // yolo
                }
                gx = ngx; // Commit the positions
                gy = ngy;

                done = gx < 0 || gx > side || gy < 0 || gy > side;
        }

        int count = 0;
        for (int i = 0; i < side * side; i++) {
                count += locations[i] ? 1 : 0;
        }
        printf("%d\n", count);

        free(locations);
        arrfree(map);
}

char* encode_location(int x, int y, Direction dir) {
        char *str = malloc(20);
        snprintf(str, 20, "%d,%d,%d", x, y, dir);
        return str;
}

void part2(const char *input) {
        /* 
         * If the guard is in the same place looking at the same direction, then a loop has been found
         */

        side = (int)(strstr(input, "\n") - input);

        bool *map = NULL;
        arrsetcap(map, side * side); // Pre-alloc

        Direction dir = UP;
        int gx, gy;
        for (unsigned long i = 0; i < strlen(input); i++) {
                char curr = input[i];
                if (curr == '\n') continue;
                arrput(map, curr == '#');
                if (curr == '^') {
                        int loc = arrlen(map) - 1; // -1 for 0 based index
                        gx = loc % side;
                        gy = loc / side;
                }
        }


        Point *
        bool done = false;
        while (!done) {
                locmap[coords_to_index(gx, gy)] = true;

                int ngx, ngy;
        reset:
                ngx = gx;
                ngy = gy;
                switch (dir) {
                case UP:
                case DOWN:
                        ngy += (dir == DOWN ? 1 : -1);
                        break;
                case RIGHT:
                case LEFT:
                        ngx += (dir == RIGHT ? 1 : -1);
                        break;
                }
                if (get_cell(map, ngx, ngy)) { // if obstruction
                        dir = (dir + 1) % 4;
                        goto reset; // yolo
                }
                gx = ngx; // Commit the positions
                gy = ngy;

                done = gx < 0 || gx > side || gy < 0 || gy > side;
        }

        int count = 0;
        for (int i = 0; i < side * side; i++) {
                count += locmap[i] ? 1 : 0;
        }
        printf("%d\n", count);

        free(locmap);
        arrfree(map);
}

int main() {
        char *input = read_stdin();
        part1(input);
        return 0;
}

