# The Minion Game
    Kevin and Stuart want to play the 'The Minion Game'.
    
    Game Rules
        Both players are given the same string, .
        Both players have to make substrings using the letters of the string .
        Stuart has to make words starting with consonants.
        Kevin has to make words starting with vowels.
        The game ends when both players have made all possible substrings.
        
    Scoring
        A player gets +1 point for each occurrence of the substring in the string S.
    
    For Example:
        String S = BANANA
        Kevin's vowel beginning word = ANAHere, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
        Your task is to determine the winner of the game and their score.
        
    Function Description
        Complete the minion_game in the editor below.
        minion_game has the following parameters:
        string string: the string to analyze
        
    Prints
        string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
        
    Input Format
        A single line of input containing the string .

Note: The string  will contain only uppercase letters: .

    Constraints
        0 < len(S) <= 10 to the power of 6

    Sample Input
        BANANA
        
    Sample Output
        Stuart 12

Note :Vowels are only defined as . In this problem,  is not considered a vowel.

#PyPy3
    def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    n = len(string)

    stuart = 0
    kevin = 0

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")