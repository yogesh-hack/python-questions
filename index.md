## Welcome to GitHub Pages

### Test case
Input : n=5 arr[n]=[3,30,34,5,9]

Output : 9533430

'''
arr=[3,30,34,5,9]
# res=int("".join(map(str,arr)))
# s=int("".join(sorted([i for i in str(res)],reverse=True)))
# print(s)
a=[]
b=[]
for i in arr:
    if(i>10):
        a.append(i)
    else:
        b.append(i)
r=sorted(a,reverse=True)
s=sorted(b,reverse=True)
m=s+r
res=int("".join(map(str,m)))
print("Output: ",res)
'''
