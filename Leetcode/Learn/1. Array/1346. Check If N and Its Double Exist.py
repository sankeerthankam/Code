def checkIfExist(arr):
    if arr.count(0) > 1:
        return True

    arr = set(arr) - {0}

    for i in arr:
        if i*2 in arr:
            return True
    return False
