#define STB_DS_IMPLEMENTATION
#include "stb_ds.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
        int x, y;
} Point;

char *encode_point(const Point *p) {
        char *str = malloc(20); // Allocate enough space for the string
        snprintf(str, 20, "%d,%d", p->x, p->y);
        return str;
}

int main() {
        struct {
                char *key;
                void *value;
        } *map = NULL;

        Point p1 = {.x = 1, .y = 2};
        Point p2 = {.x = 3, .y = 4};
        Point p3 = {.x = 1, .y = 2};

        char *key1 = encode_point(&p1);
        char *key2 = encode_point(&p2);
        char *key3 = encode_point(&p3);

        shput(map, key1, NULL);
        shput(map, key2, NULL);
        printf("%td\n", shlen(map));
        shput(map, key3, NULL);
        printf("%td\n", shlen(map));
        // Loop all keys
        for (size_t i = 0; i < shlen(map); ++i) {
                printf("%s\n", map[i].key);
        }

        // Free allocated memory
        for (size_t i = 0; i < shlen(map); ++i) {
                free(map[i].key);
        }
        shfree(map);

        return 0;
}
