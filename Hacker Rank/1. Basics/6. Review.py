# Enter your code here. Read input from STDIN. Print output to STDOUT
# Input:
# 2
# Hacker
# Rank

# Output:
# Hce akr
# Rn ak

def even_odd_str():
    test_cases = int(input())
    
    for i in range(test_cases):
        word = input()
        even_word = word[::2] 
        odd_word = word[1::2]
        print(even_word + ' ' + odd_word)

even_odd_str()
