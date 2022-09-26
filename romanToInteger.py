class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        single_value={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        dual_value={
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        sum=0
        char_list=list(s)
        while char_list:
            if len(char_list)>=2:
                dual_key=char_list[0]+char_list[1]
                if dual_value.get(dual_key):
                    sum+=dual_value[dual_key]
                    del char_list[0]
                    del char_list[0]
                elif len(char_list)>0:
                    sum+=single_value[char_list[0]]
                    del char_list[0]
            elif len(char_list)==1:
                sum+=single_value[char_list[0]]
                del char_list[0]
            if len(char_list)==0:
                return sum
        
       
    
if __name__=="__main__":
    t=Solution().romanToInt("LVIII")
    print(t)