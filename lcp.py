class Solution(object):
    def longestCommonPrefix(self,strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            prefix_str=""
            char_lists=[list(word) for word in strs]
            char_no=-1
            for each_char in char_lists[0]:
                char_no+=1
                for count in range(1,len(char_lists)):
                    current_char_list=char_lists[count]
                    if len(current_char_list)-1<char_no:
                        return prefix_str
                    elif current_char_list[char_no]!=each_char:
                        return prefix_str
                prefix_str+=each_char
                
            return prefix_str

if __name__=="__main__":
    sol=Solution()
    r=sol.longestCommonPrefix(["flower","f"])
    print("===>",r)