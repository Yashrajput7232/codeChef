import math as m
# cook your dish here
for testcase in range(int (input())):
    # n=int (input())
    l,c,p=list(map(int,input().split(' ')))
    print(m.ceil(l/c) * p)

