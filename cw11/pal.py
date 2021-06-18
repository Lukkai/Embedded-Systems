# to check if a
# string is palindrome
def isPalindrome(s):
    print("Output: " + s[::-1])
    print("Is a palindrome?: ")
    return s == s[::-1]
 

# change so the string is similar case
pal = input("Input: ").lower().replace(" ", "")
ans = isPalindrome(pal)
if ans:
    print("Yes")
else:
    print("No")