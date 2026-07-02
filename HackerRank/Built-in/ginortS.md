# ginorts
    You are given a string S.
    S contains alphanumeric characters only.
    
    Your task is to sort the string S in the following manner:
        All sorted lowercase letters are ahead of uppercase letters.
        All sorted uppercase letters are ahead of digits.
        All sorted odd digits are ahead of sorted even digits.
        
    Input Format
        A single line of input contains the String S.
        
    Constraints
        0 < len(s) < 1000

    Output Format
        Output the sorted string S.
        
    Sample Input
        Sorting1234
        
    Sample Output
        ginortS1324

# PyPy3
    s = input()

def custom_sort(c):
    if c.islower():
        return (0, c)
    elif c.isupper():
        return (1, c)
    elif c.isdigit():
        if int(c) % 2 == 1:
            return (2, c)
        else:
            return (3, c)

print(''.join(sorted(s, key=custom_sort)))
