/******************************************
Names: Dave Taveras, Marjan Chowdry, Nick Guo
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Assignment: Hw1: Large Sums
Date: February 9th, 2021
Course: CS370: Creative Problem Solving
*******************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define BUF_SIZE 80
#define RESULT_SIZE 1024

int main(int argc, char *argv[]){
    if (argc != 2) { 
        fprintf(stderr, "Usage: %s <file>\n", argv[0]); 
        exit(EXIT_FAILURE); 
    } 
    //read in the input files
    char line[BUF_SIZE];
    char result[RESULT_SIZE];
    FILE *fp = fopen(argv[1], "r");
    if (fp==NULL){
        perror("fopen");
        exit(EXIT_FAILURE);
    }
    while(fgets(line, sizeof(line), fp)){
        // if nothing in the result, which means it's the first line, put first line in the result
        if(strlen(result)==0){
            strcpy(result, line);
        } else {
            // define shortnum and large num for adding
            size_t addsize;
            int rem = 0;
            char longnum[RESULT_SIZE];
            char shortnum[BUF_SIZE];
            if (strlen(result) < strlen(line)){
                strcpy(longnum,line);
                strcpy(shortnum,result);
            } else {
                strcpy(longnum,result);
                strcpy(shortnum,line);
            }
            
            addsize = strlen(shortnum);
            while(addsize>0 && (shortnum[addsize-1]<48 || shortnum[addsize-1]>57)){
                addsize--;
            }
            
            size_t j = strlen(longnum)-1;
            while(j>0 && (longnum[j]<48 || longnum[j]>57)){
                j--;
            }
            for (int i = addsize-1; i>=0; i--){
                int a = (int)shortnum[i]-48;
                // printf("a: %d\n",a);
                int b = (int)longnum[j]-48;
                // printf("b: %d\n",b);
                int updateint = a+b;
                if (rem==1){
                    updateint++;
                    rem = 0;
                }
                if(updateint>=10){
                    rem = 1;
                    updateint = updateint % 10;
                }
                longnum[j] = (char)(updateint+48);
                j--;
            }
            // printf("longnum: %s\n",longnum);
            // printf("rem: %d\n",rem);
            while(rem==1){
                // printf("j:%ld\n",j);
                int m = j;
                // printf("m:%d\n",m);
                if(m<0){
                    memmove(longnum+1,longnum, sizeof(longnum)+1);
                    longnum[0]='1';
                    rem=0;
                } else{
                    int cur = (int)longnum[j]-48;
                    cur++;
                    // printf("cur: %d\n",cur);
                    if (cur>=10){
                        cur = cur % 10;
                    } else{
                        rem = 0;
                    }
                    longnum[j] = (char)(cur+48);
                    j--;
                }
            }
            strcpy(result, longnum);
        }
    }
    // printf("%d",result[0]=='0');
    while(result[0]=='0'){
        memmove(result,result+1,strlen(result)-1);
    }
    fclose(fp);
    fp = fopen("output.txt", "w");
    char full[BUF_SIZE] = "Full sum: ";
    fwrite(full,1,strlen(full),fp);
    fwrite(result,1,strlen(result),fp);
    char tendigit[BUF_SIZE] = "First 10 digits: ";
    fwrite(tendigit, 1, strlen(tendigit), fp);
    char firstten[BUF_SIZE];
    strncpy(firstten,result,10);
    firstten[10]='\0';
    fwrite(firstten,1,strlen(firstten),fp);
    fclose(fp);
    return EXIT_SUCCESS;
}