# Arithmetic Operators
Task
   The provided code stub reads two integers from STDIN, a and b. Add code to print three lines

   Where:
   1. The first line contains the sum of the two numbers
   2. The second line contains the difference of two numbers (first-second)
   3. The third line contains the product of two numbers

Example
a = 3
b = 5

    Print the following
        8
        -2
        15

Input Format
    The first line contains the first integer, a.
    The second line contains the second integer, b.

Constraints
    1<= a <= 10 to the power of 10
    1<= b <= 10 to the power of 10

Output Format
    Print the three lines as explained above

Sample Output 0
    5
    1
    6

Explanation 0
    3 + 2 ==> 5
    3 - 2 ==> 1
    3 * 2 ==> 6

# Python 3
if_ _name_ _=='_ _main_ _':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)