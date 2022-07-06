
# cook your dish here
for testcase in range(int (input())):
    # n=int (input())
    c,d,t=list(map(int,input().split(' ')))
    if (t%c==0 and t%d== 0):
        print('ANY')
    elif (t%c==0):
        print("CHICKEN")
    elif(t%d==0):
        print("DUCK")
    else:
        print("NONE")
