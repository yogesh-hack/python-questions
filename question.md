## Welcome to GitHub Pages



## **Competetion Questions**
### Test case
Input : n=5 arr[n]=[3,30,34,5,9]

Output : 9533430

```python
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
```
```
Output:  9533430
```


### Sum of vowel
Test Case
Input: n=3 => 1 2 3

output: 5

```python
n=3
l=[1,2,3]
dict={
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fouteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty"
}

v=['a','e','i','o','u']

def vowel(s):
    count=0
    for i in s:
        if i in v:
            count+=1
    return count
ans=0
for i in dict:
    if i in l:
        ans+=vowel(dict[i])
print(ans)
```


