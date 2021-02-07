#longest palindrome using expand around the center method


def helper(s,l,r):
    while 0<=l and r < len(s) and s[l] == s[r]:
        #making sure that l and r in range
        #the second thing we need to do is
        #check whether the charcters at l and r are equal'
        # so what we are doing is that as long as theyre equal
        # and the left and right are in their respective limits
        # the while loop runs.
        #what does the while loop do?
        # we will reduce the value of l and increase the value of r
        # we are essentially expanding the string from
        # a mid point.
        l-=1
        r+=1
    return s[l+1:r]

    

def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        # s, i, i is for odd length string
        # i.e if the palindrome is an odd palindrome.
        # s, i, i+1 is for checking for even length palindromes. 
        res = max(helper(s,i,i), helper(s,i,i+1), res, key = len)
    return res

'''
Explanation:
for each index, we assume the index as the mid point of
the largest palindrome and keep moving to the both ends of the string
using two pointers or indices

each time a palindrome length is found out
the result is stored in res

and finally the max res is returned.. this is about the expand around the
center method the time complexity is O(n^2) which is no better than dp
but the space is optimized :)
'''
print(longestPalindrome("ababa"))
        
