def caesar_cipher(input_str,step):
    input_list=list(input_str)
    ans=""
    step=step%26
    for i in input_list:
        val=ord(i)
        if val>=97 and val<=122:
            if val+step>122:
                forward=122-val
                ans=ans+chr(97+forward)
            else:
                ans=ans+chr(val+step)
        elif val>=65 and val<=90:
            if val+step>90:
                forward=90-val
                ans=ans+chr(65+forward)
            else:
                ans=ans+chr(val+step)
    return ans
print(caesar_cipher("ABxsyQaLBDashtydjdb",26))