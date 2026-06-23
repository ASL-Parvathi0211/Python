# Alphabet Rangoli
    You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

    Different sizes of alphabet rangoli are shown below:
        #size 3
            ----c----
            --c-b-c--
            c-b-a-b-c
            --c-b-c--
            ----c----
            
        #size 5
            --------e--------
            ------e-d-e------
            ----e-d-c-d-e----
            --e-d-c-b-c-d-e--
            e-d-c-b-a-b-c-d-e
            --e-d-c-b-c-d-e--
            ----e-d-c-d-e----
            ------e-d-e------
            --------e--------
            
        #size 10
            ------------------j------------------
            ----------------j-i-j----------------
            --------------j-i-h-i-j--------------
            ------------j-i-h-g-h-i-j------------
            ----------j-i-h-g-f-g-h-i-j----------
            --------j-i-h-g-f-e-f-g-h-i-j--------
            ------j-i-h-g-f-e-d-e-f-g-h-i-j------
            ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
            --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
            j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
            --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
            ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
            ------j-i-h-g-f-e-d-e-f-g-h-i-j------
            --------j-i-h-g-f-e-f-g-h-i-j--------
            ----------j-i-h-g-f-g-h-i-j----------
            ------------j-i-h-g-h-i-j------------
            --------------j-i-h-i-j--------------
            ----------------j-i-j----------------
            ------------------j------------------
            
        The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).
        
    Function Description
        Complete the rangoli function in the editor below.
        rangoli has the following parameters:
            int size: the size of the rangoli
            
    Returns
        string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
        
    Input Format
        Only one line of input containing , the size of the rangoli.
        
    Constraints
        1< size < 27
        
    Sample Input
        5
        
    Sample Output
        --------e--------
        ------e-d-e------
        ----e-d-c-d-e----
        --e-d-c-b-c-d-e--
        e-d-c-b-a-b-c-d-e
        --e-d-c-b-c-d-e--
        ----e-d-c-d-e----
        ------e-d-e------
        --------e--------

# PYPY3
    import string

def print_rangoli(size):
    alphabets = string.ascii_lowercase

    lines = []

    for i in range(size):
        left = alphabets[size-1:i:-1]
        right = alphabets[i:size]
        row = "-".join(left + right)
        lines.append(row.center(4*size-3, "-"))

    full_pattern = lines[::-1] + lines[1:]

    print("\n".join(full_pattern))
