A,B=map(int,(input().split()))
if B<45:
    if A==0:
        A=23
        B=B+60
    else:
        A=A-1
        B=B+60
print(A,B-45)