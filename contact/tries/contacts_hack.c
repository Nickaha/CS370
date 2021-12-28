#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALPHABET_LENGTH    26
#define OPERATION_BUF_SIZE  7 /* Large enough to cover the word 'search' and '\0' */
#define NAME_BUF_SIZE      22

typedef struct node {
    int prefix_count;
    /* Allocate +1 for the the pointer to the end-of-string marker. Needed
       for the search feature. */
    struct node *children[ALPHABET_LENGTH + 1];
} trie_node;

char* readline();
char** split_string(char*);

/*
 * Complete the contacts function below.
 */

/*
 * Please store the size of the integer array to be returned in result_count pointer. For example,
 * int a[3] = {1, 2, 3};
 *
 * *result_count = 3;
 *
 * return a;
 *
 */
int* contacts(char** queries, int lines, int *m){
    char** contact = (char**)malloc(NAME_BUF_SIZE*lines*sizeof(char*));
    for (int i = 0; i<lines;i++){
        contact[i] = (char*)malloc(NAME_BUF_SIZE*sizeof(char));
    }
    int* result = (int*)malloc(lines*sizeof(int));
    int j = 0;
    
    for(int i = 0; i<lines; i++){
        char* operation;
        operation = (char*)malloc(OPERATION_BUF_SIZE*sizeof(char));
        char* name = (char*)malloc(NAME_BUF_SIZE*sizeof(char));
        char* oper;
        oper = strtok(queries[i]," ");
        // printf("%s\n",oper);
        strcpy(operation,oper);
        // printf("%s\n",operation);
        oper = strtok(NULL," ");
        strcpy(name,oper);
        //printf("operation: %s\n name: %s\n",operation,name);
        if(strcmp(operation,"add")==0){
            memcpy(contact[j],name,strlen(name));
            //printf("added name:%s\n",contact[j]);
            j++;
        } else if (strcmp(operation,"find")==0){
            int count = 0;
            //printf("j: %d\n",j);
            for(int x = 0; x<j;x++){
                // printf("contact: %s\n",contact[x]);
                // printf("len of contact: %ld\n",strlen(contact[x]));
                // char temp[strlen(name)];
                // printf("len: %ld\n",strlen(name));
                // strncpy(temp,*(contact+x),strlen(name));
                // printf("temp: %s\n",temp);
                // printf("size of temp: %ld\n",strlen(temp));
                if(strncmp(contact[x],name,strlen(name))==0){
                    count++;
                }
            }
            result[*m]=count;
            *m+=1;
        } else{
            fprintf(stderr,"Invalid option\n");
        }
        free(name);
        free(operation);
    }
    for (int i = 0; i<lines;i++){
        free(contact[i]);
    }
    free(contact);
    return result;
}


int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char* queries_rows_endptr;
    char* queries_rows_str = readline();
    // printf("%s\n",queries_rows_str);
    int lines = strtol(queries_rows_str, &queries_rows_endptr, 10);
    // printf("%s\n",queries_rows_endptr);
    if (queries_rows_endptr == queries_rows_str || *queries_rows_endptr != '\0') { exit(EXIT_FAILURE); }
    char** queries = (char**)malloc(lines*(NAME_BUF_SIZE+OPERATION_BUF_SIZE)*sizeof(char*));
    for (int i = 0; i<lines;i++){
        queries[i] = (char*)malloc((NAME_BUF_SIZE+OPERATION_BUF_SIZE)*sizeof(char));
        queries[i] = readline();
        // printf("get: %s\n",queries[i]);
        if(queries[i][strlen(queries[i])-1]=='\n'){
            queries[i][strlen(queries[i])-1]='\0';
        }
    }
    int m = 0;
    int* result = contacts(queries, lines,&m);
    
    // char*** queries = malloc(queries_rows * sizeof(char**));

    // for (int queries_row_itr = 0; queries_row_itr < queries_rows; queries_row_itr++) {
    //     queries[queries_row_itr] = malloc(2 * (sizeof(char*)));

    //     char** queries_item_temp = split_string(readline());

    //     for (int queries_column_itr = 0; queries_column_itr < 2; queries_column_itr++) {
    //         char* queries_item = queries_item_temp[queries_column_itr];

    //         queries[queries_row_itr][queries_column_itr] = queries_item;
    //     }
    // }

    // int result_count=0;
    // int* result = contacts(queries_rows, 2, queries, &result_count);

    for (int result_itr = 0; result_itr < m; result_itr++) {
        fprintf(fptr, "%d", result[result_itr]);

        if (result_itr != m - 1) {
            fprintf(fptr, "\n");
        }
    }

    fprintf(fptr, "\n");

    fclose(fptr);
    for (int i = 0; i<lines;i++){
        free(queries[i]);
    }
    free(queries);
    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}
