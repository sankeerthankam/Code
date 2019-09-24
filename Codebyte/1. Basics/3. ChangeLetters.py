# For this challenge you will be manipulating characters in a string based off their positions in the alphabet.
# Change every letter by offset 1, i.e. 'a' becomes 'b', 'b' becomes 'c' .... 'z' becomes 'a'.
# Capitalize the vowels
# Ignore the special characters

def LetterChanges(word): 

    import string
    word = word.lower()
    vowels = set('aeiou')
    new_word = ''
    for i in word:
        if i in string.ascii_letters:
            if i == 'z':
                new_char = 'a'
            else:
                i = bytes(i, 'utf-8')
                new_char = bytes([i[0]+1])
                new_char = str(new_char)[2]

            if new_char in vowels:
                new_char = new_char.upper()
        else:
            new_char = i
        new_word = new_word + new_char
    return new_word

print(LetterChanges(input()))
