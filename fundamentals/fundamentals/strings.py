print("this is a sample string")

name = 5
print("My name is",name)

name = 5
print("My name is " + str(name))

first_name = "Svet"
last_name = "Pavlov"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Svet"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

x = "hello world hello helo hello"
y = "hello1"
print(x.endswith(y))
# output:
"Hello World"

