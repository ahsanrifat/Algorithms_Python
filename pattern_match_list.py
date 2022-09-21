s=["y","z","a","b","c","d","e","x","y","z","c","y","z","c","a","b","y"]
p=["x","y","z","c"]
# s=["a","b","c","a","b","c","a","b","y","a","a","b"]
# p=["a","b","c","a","b","y"]

pattern_pointer=0
s_indx=-1
for elem in s:
    s_indx+=1
    if elem==p[pattern_pointer]:
        pattern_pointer+=1
    else:
        if pattern_pointer!=0:
            # we have some matching part and then the mismatch ocurred
            while True:
                pattern_pointer-=1
                if p[pattern_pointer]==elem: 
                    # found a suffix so start matching from after that char
                    pattern_pointer+=1
                    break
                if pattern_pointer==0: break                
    if pattern_pointer-1==len(p)-1:
        print("Pattern Present")
        print(s_indx-len(p)+1)
        print(elem)
        break