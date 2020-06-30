def plusOne(digits):
    return [int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]
