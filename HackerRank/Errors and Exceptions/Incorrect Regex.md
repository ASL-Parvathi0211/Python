# Incorrect Regex
    You are given a string S.
    Your task is to find out whether S is a valid regex or not.
    
    Input Format
        The first line contains integer T, the number of test cases.
        The next  lines contains the string S.
        
    Constraints
        0 < T < 100

    Output Format
        Print "True" or "False" for each test case without quotes.
        
    Sample Input
        2
        .*\+
        .*+
        
    Sample Output
        True
        False
        
    Explanation
        .*\+ : Valid regex.
        .*+: Has the error multiple repeat. Hence, it is invalid.

# PyPy3
    import re
n = int(raw_input())
for _ in range(n):
    s = raw_input().strip()
    try:
        re.compile(s)
        print("True")
    except re.error:
        print("False")
        