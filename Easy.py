# Star problem
def pattern(n):
    for i in range(1,n+1):
        spaces= " " *(n-i)
        stars= "*"* (2*i-1)

        print (spaces+stars)

n=int(input())
pattern(n)
