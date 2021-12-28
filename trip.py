import sys
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

def lcs_dp(s1, s2, show_table=False):
    """Returns a tuple of values. Index 0 contains the length of the longest
    common subsequence, while index 1 contains the string. Uses bottom-up
    dynamic programming to improve performance."""
    rows = len(s1)
    cols = len(s2)
    # lcs = [[0] * (cols + 1) for _ in range(rows + 1)]
    stars = [[0] * (cols) for _ in range(rows)]
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if s1[r - 1] == s2[c - 1]:
                # lcs[r][c] = lcs[r - 1][c - 1] + 1
                stars[r-1][c-1] = 1
            # else:
            #     # lcs[r][c] = max(lcs[r][c - 1], lcs[r - 1][c])
    # print(stars)
    if show_table:
        # display_table(lcs)
        # print()
        display_table(stars)
    r = 0
    longest = 0
    while r < rows:
        c=0
        while c < cols:
            
def findcommon(route):
    commonroutes = []
    alice = route[0]
    bob = route[1]
    subs = {}
    lcs_dp(alice,bob,True)
        

def commontrip():
    n = input()
    case = int(n)*2
    routes = []
    for i in range(int(n)):
        alice = input()
        bob = input()
        routes.append((alice,bob))
    for tuples in routes:
        findcommon(tuples)
        # for line in result:
        #     print(line)
        # print()

commontrip()