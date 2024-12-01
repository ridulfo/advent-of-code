#include "utils.h"
#include "stb_ds.h"

#include <stdio.h>
#include <stdlib.h>

char *read_stdin() {
        char *buffer = NULL;
        char temp[1024];
        size_t bytes_read;

        while ((bytes_read = fread(temp, 1, sizeof(temp), stdin)) > 0) {
                char *dst = arraddnptr(buffer, bytes_read);
                if (!dst) {
                        perror("Memory allocation failed");
                        exit(EXIT_FAILURE);
                }
                memcpy(dst, temp, bytes_read);
        }

        // Null-terminate the final string
        arrput(buffer, '\0');
        return buffer;
}
