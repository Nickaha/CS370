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
void add(trie_node* trie,char* name){
    for(int i = 0; i<strlen(name);i++){
        int index = name[i] - 'a';
        trie->prefix_count++;
        if(trie->children[index]==NULL){
            trie->children[index] = (trie_node*) malloc(sizeof(trie_node));
		}
		trie = trie->children[index];
    }
    trie->children[ALPHABET_LENGTH] = (trie_node*) malloc(sizeof(trie_node));
	//increment the prefix count for last element
	trie->prefix_count++;
}
int find(trie_node* trie,char* name){
    //printf("Im in find\n");
    //printf("strlen of name: %ld\n",strlen(name));
    for(int i = 0; i<strlen(name);i++){
        //printf("i in find: %d\n",i);
        int index = name[i] - 'a';
        if(trie->children[index]==NULL){
            return 0;
        } else{
            trie= trie->children[index];
        }
    }
    return trie->prefix_count;
}

int search(trie_node* trie, char* name){
    for(int i = 0; i<strlen(name);i++){
        int index = name[i]-'a';
        if(trie->children[index]==NULL){
            return 0;
        } else{
            trie=trie->children[index];
        }
    }
    if(trie->children[ALPHABET_LENGTH] != NULL){
		/*if the null byte is found at end of word, 
		 that means the whole word was found return 1*/
		return 1;
	}else{
		/*if this else is met,
		  that means the input was a part 
		  of a word that's in the trie but 
		  not the whole word, return 0*/
		return 0;
	}
}


void deleteNodes(trie_node* trie){
	//delete function to prevent memory leaks
	for(int i = 0; i < ALPHABET_LENGTH + 1; i++){
		if(trie->children[i] != NULL){
			deleteNodes(trie->children[i]);
		}
	}
	free(trie);
}

int main(int argc, char *argv[])
{
    //FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");
    trie_node* trie = (trie_node*)malloc(sizeof(trie_node));
    char* queries_rows_endptr;
    // FILE *fp = fopen(argv[1], "r");
    // if (fp==NULL){
    //     perror("fopen");
    //     exit(EXIT_FAILURE);
    // }
    char queries_rows_str[OPERATION_BUF_SIZE+NAME_BUF_SIZE+1];
    fgets(queries_rows_str,(OPERATION_BUF_SIZE+NAME_BUF_SIZE+1),stdin);
    //printf("%s\n",queries_rows_str);
    int lines = strtol(queries_rows_str, &queries_rows_endptr, 10);
    //printf("%d\n",lines);
    //if (queries_rows_endptr == queries_rows_str || *queries_rows_endptr != '\0') { exit(EXIT_FAILURE); }
    char** queries = (char**)malloc(lines*(NAME_BUF_SIZE+OPERATION_BUF_SIZE)*sizeof(char*));
    //char queries[lines][NAME_BUF_SIZE+OPERATION_BUF_SIZE];
    int m = 0;
    int* result = (int*)malloc(lines*sizeof(int));
    for (int i = 0; i<lines;i++){
        //printf("%d\n",i);
        queries[i] = (char*)malloc((NAME_BUF_SIZE+OPERATION_BUF_SIZE)*sizeof(char));
        fgets(queries[i],NAME_BUF_SIZE+OPERATION_BUF_SIZE+1,stdin);
        //printf("get: %s\n",queries[i]);
        if(queries[i][strlen(queries[i])-1]=='\n'){
            queries[i][strlen(queries[i])-1]='\0';
        }
        if(queries[i][strlen(queries[i])-2]=='\r'){
            queries[i][strlen(queries[i])-2]='\0';
        }
        char* operation;
        operation = (char*)malloc(OPERATION_BUF_SIZE*sizeof(char));
        char* name = (char*)malloc(NAME_BUF_SIZE*sizeof(char));
        char* oper;
        oper = strtok(queries[i]," ");
        //printf("%s\n",oper);
        strcpy(operation,oper);
        //printf("%s\n",operation);
        oper = strtok(NULL," ");
        strcpy(name,oper);
        //printf("%s\n",name);
         if(strcmp(operation,"add")==0){
            add(trie, name);
        } else if (strcmp(operation,"find")==0){
            //printf("found!\n");
            int count = find(trie,name);
            //printf("count:%d\n",count);
            result[m] = count;
            //printf("result of find: %d\n",result[m]);
            m++;
        } else if (strcmp(operation,"search")==0){
            int boolval = search(trie,name);
            if(boolval==1){
                result[m]=-2;
            } else{
                result[m]=-3;
            }
            m++;
        }
        //printf("i: %d\n",i);
    }
    
    //printf("%d\n",m);
    for (int result_itr = 0; result_itr < m; result_itr++) {
        // printf("result:%d\n",result[result_itr]);
        if(result[result_itr]>=0){
            printf("%d\n",result[result_itr]);
            
            //fprintf(fptr, "%d", result[result_itr]);
        }
        else{
            if(result[result_itr]==-2){
                printf("yes\n");
                //fprintf(fptr, "yes");
            } else{
                printf("no\n");
                //fprintf(fptr,"no");
            }
        }
        // if (result_itr != m - 1) {
        //     fprintf(fptr, "\n");
        // }
    }

    // fprintf(fptr, "\n");

    // fclose(fptr);
    for (int i = 0; i<lines;i++){
        free(queries[i]);
    }
    free(queries);
    deleteNodes(trie);
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
