def isAdditiveNumber(self, num: str) -> bool:
    # Create a combinations of indices to create num1 and num2
    # i.e. for a number '112358'
    # all number combinations are 
    # [(1, 1), (1, 12), (1, 123)...]
    # [(1, 2), (1, 23), (1, 234)...]
    # [(2, 3), (2, 35), (2, 358)...]
    # and so on
    # Check if num1 or num2 starts with 0 -> If so avoid the current iteration
    # Check if the sum of the tuple (or a sum of the num1, num2) is equal 
        # swap num1 and num2 with num2 and sum
        # move the 'j' pointer by len(c) digits

    from itertools import combinations
    n = len(num)
    all_indices = [i for i in range(1, n)]
    for i, j in combinations(all_indices, 2):
        a, b = num[:i], num[i:j]
        # Check if either num1 or num2 has leading 0s
        if a != str(int(a)) or b != str(int(b)):
            continue
        while j < n:
            c = str(int(a) + int(b))
            if num.startswith(c, j):
                # if you see the sum ('c') in the 'num' at position[j]
                    # swap a and b with b and c
                    # move the 'j' pointer by len(c) digits
                j += len(c)
                a, b = b, c

            else:
                break

        # If the second pointer has reached the end of the string - return true
        if j == n:
            return True
    return False
