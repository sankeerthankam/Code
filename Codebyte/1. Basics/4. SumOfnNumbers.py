# Sum of n numbers

def SimpleAdding(num): 

    sum = 0
    for i in range(num+1):
        if i > 0:
            sum = sum + i
    return sum
    
print(SimpleAdding(input()))
