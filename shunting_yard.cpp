#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main(int args, char** argv[]){
    fstream fp;
    fp.open(argv[1],ios::in);
    if(!fp.is_open()){
        cerr<< "can't open file"<<endl;
        return 1;
    }
    //char preference[] = {'+', '-', '*', '/', '^'};
    string tp;
    getline(fp,tp);
    stringstream conv(tp);
    int lines = 0;
    conv >> lines;
    vector<char> queue;
    vector<char> s;
    for (int i = 0; i< lines; i++){
        string line;
        getline(fp,line);
        for(int j = 0; j<line.length();j++){
            char X = line[i];
            if( (X == '/') || (X == '*') || (X == '+') || (X == '-') || (X== '^')){
                //add X to output
                s.push_back(X);
            }
            else if( islower(X)) {
                // if ( (!islower(s.end())) && (X.priority < s.end.priority)){
                // s.pop;
                // //add s.end to output
                //  }
                // //add X to output
                queue.push_back(X);
            }
            else if( X == '(' ){
                //push onto stack
                s.push_back(X);
            }
            else if( X == ')'){
                while (s.end() != '('){
                    queue.push_back(s.end());
                }
            //stack.pop (pop ')' and do not add to output
            }
        while (s.length != 0) {}
        //pop rest of stack and add to output
        }
    }
    return 0;
}


//+, -, *, /, ^  (priority from the lowest to the highest)

/*******************************************************************************
 * Shunting-yard algorithm
 *   Simplified version that works with well-formed infix expressions only.
 *   No error handling.
 *
 * While there are tokens to be read:
 *     Read a token.
 *     If the token is an operand, add it to the output queue.
 *     If the token is an operator, o1:
 *         While there is an operator token, o2, at the top of the stack and
 *         o1's precedence is less than or equal to that of o2:
 *             Pop o2 off the stack and add it to the output queue.
 *         Push o1 onto the stack.
 *     If the token is a left parenthesis, push it onto the stack.
 *     If the token is a right parenthesis:
 *         Until the token at the top of the stack is a left parenthesis, pop
 *         operators off the stack and add them to the output queue.
 *         Pop the left parenthesis from the stack, but not do not add it to
 *         the output queue.
 * When there are no more tokens to read:
 *     While there are still operator tokens in the stack:
 *         Pop the operator from the stack and add it to the output queue.
 ******************************************************************************/

/**
begin() – Returns an iterator pointing to the first element in the vector
end() – Returns an iterator pointing to the theoretical element that follows the last element in the vector
rbegin() – Returns a reverse iterator pointing to the last element in the vector (reverse beginning). It moves from last to first element
rend() – Returns a reverse iterator pointing to the theoretical element preceding the first element in the vector (considered as reverse end)
cbegin() – Returns a constant iterator pointing to the first element in the vector.
cend() – Returns a constant iterator pointing to the theoretical element that follows the last element in the vector.
crbegin() – Returns a constant reverse iterator pointing to the last element in the vector (reverse beginning). It moves from last to first element
crend() – Returns a constant reverse iterator pointing to the theoretical element preceding the first element in the vector (considered as reverse end)
 * 
 */