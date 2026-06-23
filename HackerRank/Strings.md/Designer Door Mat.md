# Designer Door Mat
    Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
    
    Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format
    A single line containing the space separated values of  and .

Constraints
    5 < N < 101
    15 < M < 303

Output Format
    Output the design pattern.

Sample Input
    9 27

Sample Output

 ------------.|.------------
 ---------.|..|..|.---------
 ------.|..|..|..|..|.------
 ---.|..|..|..|..|..|..|.---
 ----------WELCOME----------
 ---.|..|..|..|..|..|..|.---
 ------.|..|..|..|..|.------
 ---------.|..|..|.---------
 ------------.|.------------

# Python 3
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    N, M = map(int, input().split())

    pattern = ".|."

    # Top half
    for i in range(N // 2):
    print((pattern * (2 * i + 1)).center(M, '-'))
    
    # Middle line
    print("WELCOME".center(M, '-'))
    
    # Bottom half
    for i in range(N // 2 - 1, -1, -1):
    print((pattern * (2 * i + 1)).center(M, '-'))
