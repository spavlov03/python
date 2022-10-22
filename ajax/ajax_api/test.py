# def reverse(str):
#     if len(str) == 0:
#         return str
#     return reverse(str[1:]) + str[0]
# print(reverse("Hello"))

# find Palindrome : madam,radar,mom

def palindrome(list): 
    for word in list: 
        if word == word[::-1]: 
            print("yes",word)
            # print(word[::-1]) - [::-1] reverses string 
        else : 
            print("no",word)

palindrome(["test","car","madam","radar","mom","rocket","malayalam","catnintac"])
# palindrome("radar")