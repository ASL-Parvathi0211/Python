# Integers Come In All Sizes
    Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: 2 to the power of 31 -1 (c++ int) or 2 to the power of 63 -1 (C++ long long int).
    As we know, the result of  grows really fast with increasing b.
    Let's do some calculations on very large integers.
    
    Task
        Read four numbers, a, b, c, and d, and print the result of a power b+ c power d.
    
    Input Format
        Integers a, b, c, and d are given on four separate lines, respectively.
        
    Constraints
        1 <= 1 <= 1000
        1 <= b <= 1000
        1 <= c <= 1000
        1 <= d <= 1000
        
    Output Format
        Print the result of a power b + c power d on one line.
        
    Sample Input
        9
        29
        7
        27
    
    Sample Output
        4710194409608608369201743232  

Note: This result is bigger than 2 to the power of 63-1. Hence, it won't fit in the long long int of C++ or a 64-bit integer.

# PyPy3
     a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(pow(a, b) + pow(c, d))
