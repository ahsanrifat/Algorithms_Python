from typing import Optional
class Solution:
    min_len=100000000
    def get_height(self,n,length,root):
        if n>=length:
            return -1
        left=self.get_height(2*n+1,length,root)
        right=self.get_height(2*n+2,length,root)
        if min(left,right)+1>1 and min(left,right)<self.min_len:
            self.min_len=min(left,right)
        return min(left,right)+1
    def maxDepth(self, root) -> int:
        self.get_height(0,len(root),root)
        return self.min_len
    
if __name__=="__main__":
    print(Solution().maxDepth([3,9,20,None,None,15,7]))
    