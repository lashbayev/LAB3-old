def is_palindrome(s):
    cleaned_str = ''.join(s.split()).lower()

    return cleaned_str == cleaned_str[::-1]


print(is_palindrome("madam"))  
print(is_palindrome("racecar"))  
print(is_palindrome("hello"))  
print(is_palindrome("A man a plan a canal Panama"))  
