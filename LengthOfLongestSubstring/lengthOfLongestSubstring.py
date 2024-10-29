s = "abcabcbb"

def lengthOfLongestSubstring(s):
        if len(s) == 0:
            return 0

        max_len = 1
        s_start = 0
        for i in range(1, len(s)):#loop start from second element
            if s[i] not in s[s_start:i]:#check for each element if is not in the remaining substring
                max_tmp = i - s_start + 1
                max_len = max(max_len, max_tmp)#compare the current temp and the previous
            else:
                #if it is in, then get a new start!
                s_start = s[s_start:i].index(s[i]) + s_start + 1
                max_tmp = i - s_start + 1
                max_len = max(max_len, max_tmp)#compare the current temp and the previous

        return max_len

print(lengthOfLongestSubstring(s))