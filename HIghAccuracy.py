# cook your dish here
for testcase in range(int (input())):
    N=int(input())
    if (N%3==0):
         print(0)
    else:
        n=N
        N=N//3 +1
        print(N*3-n)
