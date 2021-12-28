'''
Names: Dave Taveras, Marjan Chowdhury, Nick Guo
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Assignment: Hw6: SPOJ 33: TRIP
Date: March 30th, 2021
Course: CS370: Creative Problem Solving
'''

# code from class used for seeing how the table looks
def display_table(T):
    """Displays matrix T on the screen formatted as a table."""
    r = len(T)
    c = len(T[0])
    max_val = 0
    for row in range(r):
        for col in range(c):
            if not T[row][col] is None and T[row][col] > max_val:
                max_val = T[row][col]
    max_cell_width = len(str(max(c, r, max_val)))
    sys.stdout.write(' ' * len(str(r)))
    for col in range(c):
        sys.stdout.write(' ' + str(col).rjust(max_cell_width))
    sys.stdout.write('\n')
    for row in range(r):
        sys.stdout.write(str(row).rjust(max_cell_width))
        for col in range(c):
            if T[row][col] is None:
                sys.stdout.write(' -')
            else:
                sys.stdout.write(' ' + str(T[row][col]).rjust(max_cell_width))
        sys.stdout.write('\n')

'''
def backtrack(s1, s2, i, j, table, sequences, word):
    if(substrings[i][j].find(word)!=substrings[i][j].end())
    return;
  if i==0 or j==0:
    sequences.insert(word);
    // printf("%s\n",word.c_str());
  else if(s1[i-1]==s2[j-1])
  {
    word = s1[i-1] + word;
    backtrack(s1,s2,i-1,j-1,table,sequences,word);
  }
  else if table[i][j-1]>table[i-1][j]:
    backtrack(s1,s2,i,j-1,table,sequences,word)
  else if table[i-1][j]>table[i][j-1]:
    backtrack(s1,s2,i-1,j,table,sequences,word)
  else
    backtrack(s1,s2,i,j-1,table,sequences,word)
    backtrack(s1,s2,i-1,j,table,sequences,word)
  substrings[i][j][word] = true
'''

# a is alice's list of cities, b is bob's list
def trip(a, b, show_table=False):
    # initalize table and fill in like in class
    rows = len(a)
    cols = len(b)
    t = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if a[r - 1] == b[c - 1]:
                t[r][c] = t[r - 1][c - 1] + 1
            else:
                t[r][c] = max(t[r][c - 1], t[r - 1][c])
    if show_table:
        display_table(t)
    solutions = []
    s = ''
    r = rows
    c = cols
    def string_builder(r,c,s):
        while r > 0 and c > 0:
            if s1[r - 1] == s2[c - 1]:
                s = s1[r - 1] + s
                r -= 1
                c -= 1
            elif lcs[r][c - 1] >= lcs[r - 1][c]:
                c -= 1
            else:
                r -= 1

    
    

    for s in solutions: print(s)

    


if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        a = input()
        b = input()
        trip(a, b)
