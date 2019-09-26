# This challenge requires you to determine if every alphabetic character in a string has a plus (+) symbol on the left and 
# right side of itself. For example: the string "+a+b+c+" is good but the string "===+3+f=+b+" is not because the "f" does 
# not have a plus symbol to its right. A very simple way to solve this challenge is to create a loop that every time it gets 
# to an alphabetic character, it checks to see if it is surrounded by + symbols.

def SimpleSymbols(a): 
  
    ls = []
    for i in a:
        if len(a) > 2:
            if i.isalpha():
                if a.index(i) != 0:
                # print(i)
                    if a[a.index(i)+1] == '+' and a[a.index(i)-1] == '+':
                        ls.append(True)
                    else:
                        return False
                else:
                    return False
            else:
                continue
        else:
            return False
        
    if False in ls:
        return False
    else:
        return True

# keep this function call here  
print(SimpleSymbols(input()))
