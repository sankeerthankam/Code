def maxProfit(arr):

    if len(arr) == 0:
        return 0

    max_profit = arr[0]
    min_so_far = arr[0]
    ls = []
    for i in arr:
        max_profit = i - min_so_far

        if i < min_so_far:
            min_so_far = i
        ls.append(max_profit)

    if max(ls) > 0:
        return max(ls) 
    else:
        return 0
