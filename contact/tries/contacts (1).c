/******************************************
Names: Dave Taveras, Marjan Chowdhury, Nick Guo
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Assignment: Hw3: Trie Contacts
Date: February 23rd, 2021
Course: CS370: Creative Problem Solving
*******************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ALPHABET_LENGTH    26
#define OPERATION_BUF_SIZE  7 /* Large enough to cover the word 'search' and '\0' */
#define NAME_BUF_SIZE      22

/* Basic trie node -- also, keep track of number of nodes below this one. */
typedef struct node {
    int prefix_count;
    /* Allocate +1 for the the pointer to the end-of-string marker. Needed
       for the search feature. */
    struct node *children[ALPHABET_LENGTH + 1];
} trie_node;

void add(char* str, trie_node* trie){
	//function to add word to trie
	int i = 0;
	for(i; i < strlen(str); i++){
		//get the next char index 
		int index = str[i] - 'a';
		//increment prefix_count for new work
		trie->prefix_count++;
		if(trie->children[index] == NULL){
			//if the child at index is null make a new one
			trie->children[index] = (trie_node*) malloc(sizeof(trie_node));
		}
		trie = trie->children[index];
	}
	//make a new node at \0 index to show end of string is reached
	trie->children[ALPHABET_LENGTH] = (trie_node*) malloc(sizeof(trie_node));
	//increment the prefix count for last element
	trie->prefix_count++;
}



int find(char* str, trie_node* trie){
	//function to find matches in trie
	int index = 0;
	for(int i = 0; i < strlen(str); i++){
		//get the index for the next char
		index = str[i] - 'a';
		if(trie->children[index] == NULL){
			// if the index of that char is null then there were no matches
			return 0;
		}else{
			// continue traversing
			trie = trie->children[index];
		}
	}
	return trie->prefix_count;
}

int search(char* str, trie_node* trie){
	//function to search for exact word in trie
	int index = 0;
	for(int i = 0; i < strlen(str); i++){
		index = str[i] - 'a';
		if(trie->children[index] == NULL){
			/*if any of the children indexes are null
			  That means that the word given is not present
			  in the trie*/
			return 0;
		}else{
			//move onto next node
			trie = trie->children[index];
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

void readInput(trie_node* trie, int* out, int ind){
	int index = 0;
	int size = 0;
	char ch;
	//create a buffer with maximum possible input
	char buf[NAME_BUF_SIZE + OPERATION_BUF_SIZE];
	//fill in the buffer
	while(1){
		ch = getchar();
		if(ch == EOF || ch == '\n'){
			//if new line was read put null byte at end
			buf[index] = '\0';
			size++;
			break;
		}else{
			//place the character in the buffer
			buf[index] = ch;
		}
		//increment size and index
		size++;
		index++;
	}
	//read the buffer
	if(buf[0] = 'a' && buf[1] == 'd' && buf[2] == 'd'){
		//call the add function
		size -= 4;
		index = 0;
		char sub[size];
		//read the rest of the buffer not including "add" and the space
		for(int i = 4; i < size + 4; i++){
			sub[index] = buf[i];
			index++;
		}
		add(sub, trie);
		
	}
	else if(buf[0] = 'f' && buf[1] == 'i' && buf[2] == 'n' && buf[3] == 'd'){
		//call the find function
		size-=5;
		index = 0;
		char sub[size];
		//read the rest of the buffer not including "find" and the space
		for(int i = 5; i < size + 5; i++){
			sub[index] = buf[i];
			index++;
		}
		out[ind] = find(sub, trie);
	}
	else if(buf[0] = 's' && buf[1] == 'e' && buf[2] == 'a' && buf[3] == 'r' 
		&& buf[4] == 'c' && buf[5] == 'h'){
		//call the search function
		size-=7;
		index = 0;
		char sub[size];
		//read the rest of the buffer not including "search" and the space
		for(int i = 7; i < size + 7; i++){
			sub[index] = buf[i];
			index++;
		}
		 
		 if (search(sub, trie) == 0){
		 	//word was not found 
		 	out[ind] = -2;
		 }else{
		 	out[ind] = -3;
		 }
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

int main(int argc, char** argv){
	//create new trie
	trie_node* trie = (trie_node*) malloc(sizeof(trie_node));
	//read initial num value for proceding lines
	int num = 0;
	scanf("%d", &num);
	int out[num];
	for(int i = 0; i < num; i++){
		out[i] = -1;
	}
	int index = 0;
	while(num >= 0){
		//read and parse inputs
		readInput(trie, out, index);
		num--;
		index++;
	}
	for(int i = 0; i < index; i++){
		if(out[i] != -1 && out[i] != -2 && out[i] != -3){
			printf("%d\n", out[i]);
		}
		else if(out[i] == -2){
			printf("no\n");
		}
		else if(out[i] == -3){
			printf("yes\n");
		}
	}
	//delete all used memory
	deleteNodes(trie);
	return 0;
}
