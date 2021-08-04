'''
my_str = input("Enter your value: ")
print(my_str)



my_str = my_str.casefold()


rev_str = reversed(my_str)


if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


'''

#The process in which a function calls itself directly or
#indirectly is called recursion and the
#corresponding function is called as recursive function.
#the function containing recursion is called recursive function


'''
1. User must enter a string.
2. The string is passed as an argument to a recursive function.
3. In the function, if the length of the string is less than 1, True is returned.
4. If the last letter is equal to the first letter, the function is called
recursively with theargument as the sliced list with the first character
and last character removed, else return False.
5. The if statement is used to check if the returned value is
True or False and the final result is printed.
'''
def is_it_a_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_it_a_palindrome(s[1:-1])
        else:
            return False


        
a=str(input("Enter string:"))
if(is_it_a_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")
