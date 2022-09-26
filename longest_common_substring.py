nums1=list("ABCDXYZABCDDEF")
nums2=list("ABCDQYZABCDDEMKK")

# making sure that nums1 is the largest one 
if len(nums1)<len(nums2):
    temp=nums1
    nums1=nums2
    nums2=temp

# making the DP array
dp_array=[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
# (index,number_of_matched_characters)
max_=(None,0)
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i]==nums2[j]:
            new_substring_len=dp_array[i-1][j-1]+1
            dp_array[i][j]= new_substring_len
            if max_[1]<new_substring_len:
                max_=(i,new_substring_len)
                
end=max_[0]-len(nums1)
start=end-(max_[1]-1)
if end>=-1:
    end=None
elif end<=-2:
     end=end+1   
print(f"The match ends at the index of {max_[0]} of the longest string")
print(f"Numbers of matched characters {max_[1]}")  
print(f"Slice starts at {start} and ends at {end} of the longest string")
print("The matched substring -> ","".join(n for n in nums1[start:end]))
    