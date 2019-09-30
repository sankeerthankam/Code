# Enter your code here. Read input from STDIN. Print output to STDOUT

num = int(input())

for i in range(1, 11):
    # print(num, "x", i, "=", num*i)
    print('{0} x {1} = {2}'.format(num, i, num*i))
