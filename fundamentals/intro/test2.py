# create a function that will take in a number as an input and return array contains all the numbers
# from 1 to that number if the number is divisible by 3 print fizz
# if its divisible by 5 print buzz
# if it divided by both print fizzbuzz
# return a list contain the output

def fizz_buzz(num):
    result = []
    for i in range(1,num+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0: 
            result.append("fizz")
        elif i % 5 == 0: 
            result.append("buzz")
        else: 
            result.append(i)
    return result

the_result = fizz_buzz(30)
print(the_result)