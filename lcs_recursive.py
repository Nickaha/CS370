"""
Name          : lcs_recursive.py
Author        : Brian S. Borowski
Version       : 1.2
Date          : February 26, 2018
Last modified : March 23, 2021
Description   : Longest common subsequence implemented with recursion and
                memoization.
"""
import time

def lcs(s1, s2):
    """Returns the length of the longest common subsequence between strings
    s1 and s2."""
    if s1 == '' or s2 == '':
        return 0
    if s1[0] == s2[0]:
        return 1 + lcs(s1[1:], s2[1:])
    return max(lcs(s1[1:], s2), lcs(s1, s2[1:]))

def fast_lcs(s1, s2):
    """Returns the length of the longest common subsequence between strings
    s1 and s2. Uses memoization to improve performance."""
    def fast_lcs_helper(s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        if s1 == '' or s2 == '':
            result = 0
        elif s1[0] == s2[0]:
            result = 1 + fast_lcs_helper(s1[1:], s2[1:], memo)
        else:
            result = max(fast_lcs_helper(s1[1:], s2, memo),
                         fast_lcs_helper(s1, s2[1:], memo))

        memo[(s1, s2)] = result
        return result
    return fast_lcs_helper(s1, s2, {})

def fast_lcs2(s1, s2):
    """Returns the length of the longest common subsequence between strings
    s1 and s2. Uses memoization to improve performance but avoids
    passing the dictionary to the helper function."""
    memo = {}
    def fast_lcs_helper(s1, s2):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        if s1 == '' or s2 == '':
            result = 0
        elif s1[0] == s2[0]:
            result = 1 + fast_lcs_helper(s1[1:], s2[1:])
        else:
            result = max(fast_lcs_helper(s1[1:], s2),
                         fast_lcs_helper(s1, s2[1:]))

        memo[(s1, s2)] = result
        return result
    return fast_lcs_helper(s1, s2)

def fast_lcs3(s1, s2):
    """Returns the length of the longest common subsequence between strings
    s1 and s2. Uses memoization to improve performance. This version
    uses the starting index of each string as the key for the dictionary.
    """
    memo = {}
    len1 = len(s1)
    len2 = len(s2)
    def fast_lcs_helper(start1, start2):
        if (start1, start2) in memo:
            return memo[(start1, start2)]
        if start1 == len1 or start2 == len2:
            result = 0
        elif s1[start1] == s2[start2]:
            result = 1 + fast_lcs_helper(start1 + 1, start2 + 1)
        else:
            result = max(fast_lcs_helper(start1 + 1, start2),
                         fast_lcs_helper(start1, start2 + 1))

        memo[(start1, start2)] = result
        return result
    return fast_lcs_helper(0, 0)

def fast_lcs_with_values(s1, s2):
    """Returns a tuple of values. Index 0 contains the length of the longest
    common subsequence, while index 1 contains the string. Uses memoization to
    improve performance."""
    def fast_lcs_helper(s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]

        if s1 == '' or s2 == '':
            result = (0, '')
        elif s1[0] == s2[0]:
            lose_both = fast_lcs_helper(s1[1:], s2[1:], memo)
            result = (1 + lose_both[0], s1[0] + lose_both[1])
        else:
            use_S1 = fast_lcs_helper(s1, s2[1:], memo)
            use_S2 = fast_lcs_helper(s1[1:], s2, memo)
            result = use_S1 if use_S1[0] > use_S2[0] else use_S2

        memo[(s1, s2)] = result
        return result
    return fast_lcs_helper(s1, s2, {})

def lis(s):
    """Quick and dirty way to find the longest increasing subsequence in a
    string. Simply compute the longest common subsequence between the string    itself and the string that results after removing duplicate characters and
    sorting the remaining characters."""
    return fast_lcs_with_values(s, ''.join(sorted(set(s))))

def lis2(s, t):
    """Quick and dirty way to find the longest increasing subsequence between
    two strings. Keep only the characters that are common to both strings.
    Then compute the LIS of each string and finally the LCS of those
    intermediate results."""
    s_set = set(s)
    t_set = set(t)
    inter = s_set.intersection(t_set)
    for val in list(s_set):
        if not val in inter:
            s_set.remove(val)
    for val in list(t_set):
        if not val in inter:
            t_set.remove(val)
    s_res = fast_lcs_with_values(s, ''.join(sorted(s_set)))
    t_res = fast_lcs_with_values(t, ''.join(sorted(t_set)))
    return fast_lcs_with_values(s_res[1], t_res[1])

print(lcs('aba', 'aaa'))

print(fast_lcs('aba', 'aaa'))

print(fast_lcs('daksfgsakjdgfkahdgfkjahriefdsaf',
               'asdjfhglkwehgfrkjasdhgfkjadhkad'))
start = time.time()
for _ in range(100):
    fast_lcs('daksfgsakjdgfkahdgfkjahriefdsaf',
             'asdjfhglkwehgfrkjasdhgfkjadhkad')
print("fast_lcs: %s seconds" % (time.time() - start))

print(fast_lcs2('daksfgsakjdgfkahdgfkjahriefdsaf',
                'asdjfhglkwehgfrkjasdhgfkjadhkad'))
start = time.time()
for _ in range(100):
    fast_lcs2('daksfgsakjdgfkahdgfkjahriefdsaf',
              'asdjfhglkwehgfrkjasdhgfkjadhkad')
print("fast_lcs2: %s seconds" % (time.time() - start))

print(fast_lcs3('daksfgsakjdgfkahdgfkjahriefdsaf',
                'asdjfhglkwehgfrkjasdhgfkjadhkad'))
start = time.time()
for _ in range(100):
    fast_lcs3('daksfgsakjdgfkahdgfkjahriefdsaf',
              'asdjfhglkwehgfrkjasdhgfkjadhkad')
print("fast_lcs3: %s seconds" % (time.time() - start))

print(fast_lcs_with_values(
        'daksfgsakjdgfkahdgfkjahriefdsaf',
        'asdjfhglkwehgfrkjasdhgfkjadhkad'))
start = time.time()
for _ in range(100):
    fast_lcs_with_values(
        'daksfgsakjdgfkahdgfkjahriefdsaf',
        'asdjfhglkwehgfrkjasdhgfkjadhkad')
print("fast_lcs_with_values: %s seconds" % (time.time() - start))

print(lis('zyxcba'))
print(lis('abxac'))

print(lis2('abcdeljkmn', 'rstuvjkmn'))
print(lis2('abcdefzhijk', 'hijk'))
print(lis2('lmnopqrsabcde' , 'abcde'))
print(lis2('albmcndoepqrs', 'abcde'))
