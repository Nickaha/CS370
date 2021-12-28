/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node *flatten_h(Node *parent, Node *ch){
        parent->next = ch;
        ch->prev = parent;
        parent->ch = nullptr;
        while(ch->next != nullptr){
            if(ch->child){
                flatten_h(ch,ch->child);
            }
            
        }
    }
    Node* flatten(Node* head) {
        Node* result = head;
        Node* temp;
        while(*result->next != nullptr){
            *temp = *h->next;
            if(h->child){
                h->next = flatten(h->child);
                h->chile = nullptr;
            }
            
            
        }

        return result;
    }
};