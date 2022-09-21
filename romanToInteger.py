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
            "XL":50,
            "XC":90,
            "CD":400,
            "CM":900
        }
        sum=0
        char_list=list(s)
        for count in range(len(char_list)-2):
            dual_key=char_list[count]+char_list[count+1]
            if dual_key in dual_value:
                sum+=dual_value[dual_key]
                char_list[count]=12
                if count+1==len(char_list)-1:
                    char_list[count+1]=12
        for char in char_list:
            sum+=single_value.get(char) or 0
        return sum