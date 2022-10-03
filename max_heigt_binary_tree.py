from typing import Optional
class Solution:
    def get_height(self,n,length):
        if n>=length:
            return 0
        left=self.get_height(2*n+1,length)
        right=self.get_height(2*n+2,length)
        return max(left,right)+1
    def maxDepth(self, root) -> int:
        return self.get_height(0,len(root))
    
if __name__=="__main__":
    print(Solution().maxDepth([1,None,2]))