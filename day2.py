 def maximumOddBinaryNumber(self, s: str) -> str:
        
        # ones = s.count('1')-1
        # res=''
        # zeros =s.count('0')
        # while ones > 0:
        #     res +=str(1)
        #     ones-=1
        # while zeros > 0:
        #     res+=str(0)
        #     zeros-=1
        # return res +'1'
        ones = s.count('1') - 1
        zeros = s.count('0')

        return ('1' * ones) + ('0' * zeros) + '1'
