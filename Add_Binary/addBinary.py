class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        len_a = len(a)
        len_b = len(b)
        carry = 0

        max_len = max(len_a, len_b)
        a = a.zfill(max_len)#fill in bits
        b = b.zfill(max_len)

        for i in range(max_len - 1, -1, -1):#reverse
            temp = int(a[i]) + int(b[i]) + carry
            if temp >= 2:
                carry = 1
                result = str(temp - 2) + result
            else:
                carry = 0
                result = str(temp) + result

        if carry == 1:
            result = "1" + result

        return result
