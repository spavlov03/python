def sum_nums(n):
  sum = 0
  for i in range(1,n+1):
    sum += i
  return sum

# 1 + 2 + 3 + 4
print(sum_nums(4))


def sum_nums_rec(n):
  if n == 1:
      return 1
  return n + sum_nums_rec(n - 1)

print(sum_nums_rec(4))


# 4! = 4*3*2*1 => 24

def factorial(n):
  result = 1
  for i in range(1,n+1):
    result *= i
  return result

print(factorial(4))


def factorial_rec(n):
  if n == 1:
    return 1
  return n * factorial_rec(n - 1)

print(factorial_rec(4))


# Hello => olleH
def reverse(str):
  result = ""
  for i in range(len(str),0,-1):
    result += str[i - 1]
  return result

print(reverse("Hello"))


def reverse_rec(str):
  if len(str) == 0:
    return str
  return reverse_rec(str[1:]) + str[0]



print(reverse_rec("Hello"))





# find Palindrome 
# madam,
# radar,
#  mom