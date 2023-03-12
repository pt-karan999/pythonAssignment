def anagrams(a,b):
    if(len(a)!=len(b)):
        return False
    cnt={}
    for c1, c2 in zip(a,b):
        if c1 in cnt.keys():
          cnt[c1] += 1
        else:
          cnt[c1] = 1
        if c2 in cnt.keys():
          cnt[c2] -= 1
        else:
          cnt[c2] = -1
    for c in cnt.values():
        if c!= 0:
            return False
    return True
a=input("enter first string")
b=input("enter second string")
if(anagrams(a,b)):
    print(f"the strings {a} and {b} are anagram")
else:
    print(f"the strings {a} and {b} are not anagram")