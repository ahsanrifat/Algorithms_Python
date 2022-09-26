


class Solution(object):
    def intToRoman(self, num):
        divisor_range_map={1:[9,5,4,1],2:[90,50,40,10],3:[900,500,400,100],4:[1000]}
        roman_value={
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }
        roman=""
        while num!=0:
            num_len=len(str(num))
            divisor_checking_range=divisor_range_map[num_len]
            divisor_final=None
            for divisor in divisor_checking_range:
                result=int(num/divisor)
                if result>=1:
                    divisor_final=divisor
                    break
            roman+=roman_value[divisor_final]*result
            num=num-result*divisor
        return roman
if __name__=="__main__":
    print(Solution().intToRoman(1994))