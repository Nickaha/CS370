"""
Name          : lcs_dp.py
Author        : Brian S. Borowski
Version       : 1.2
Date          : March 1, 2018
Last modified : March 23, 2021
Description   : Longest common subsequence implemented with dynamic programming.
"""
import sys
import time

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
    lcs = [[0] * (cols + 1) for _ in range(rows + 1)]
    print(s1)
    print(s2)
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if s1[r - 1] == s2[c - 1]:
                lcs[r][c] = lcs[r - 1][c - 1] + 1
            else:
                lcs[r][c] = max(lcs[r][c - 1], lcs[r - 1][c])

    if show_table:
        display_table(lcs)

    s = ''
    r = rows
    c = cols
    while r > 0 and c > 0:
        if s1[r - 1] == s2[c - 1]:
            s = s1[r - 1] + s
            r -= 1
            c -= 1
        elif lcs[r][c - 1] >= lcs[r - 1][c]:
            c -= 1
        else:
            r -= 1

    return len(s), s

# print(lcs_dp('aba', 'aaa'))
# print(lcs_dp('abaca', 'aacab', True))

# print(lcs_dp('daksfgsakjdgfkahdgfkjahriefdsaf',
#              'asdjfhglkwehgfrkjasdhgfkjadhkad', True))
# start = time.time()
# for _ in range(100):
#     lcs_dp('daksfgsakjdgfkahdgfkjahriefdsaf',
#            'asdjfhglkwehgfrkjasdhgfkjadhkad', False)
print(lcs_dp('acbacba','abcabcaa',True))
#print('lcs_dp: %s seconds' % (time.time() - start))
