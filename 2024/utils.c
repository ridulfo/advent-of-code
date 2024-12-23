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

/** Split a string into an array of strings based on a delimiter. */
char **split_str(const char *str, const char *substr) {
        size_t substr_len = strlen(substr);
        char **arr = NULL;

        const char *start = str;
        const char *match;

        while ((match = strstr(start, substr)) != NULL) {
                size_t token_len = match - start;
                char *token = strndup(start, token_len); // Copy the token
                arrput(arr, token);         // Add token to the array
                start = match + substr_len; // Move past the match
        }

        // Add the last token if any
        if (*start != '\0') {
                arrput(arr,
                       strdup(start)); // Add the remaining part of the string
        }

        return arr;
}

void splitfree(char **arr) {
        for (int i = 0; i < arrlen(arr); i++) {
                free(arr[i]);
        }
        arrfree(arr); // Free the array itself
}
