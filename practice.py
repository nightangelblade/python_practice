# Practice declaring various objects as variables
test_variable = "This is a test variable"
test_boolean = True
test_integer = 1000
test_float = 3.14
test_array = ["this", "is", "a", "test", "array"]
test_hash = {'a': 1, 'b': 2, 'c': 3}

print(test_variable)
print(test_boolean)
print(test_integer)
print(test_float)
print(test_array)
print(test_hash)
print(1 == 1)
print(1 == 2)

# Practice declaring if statement
if (test_integer > test_float):
	print("Integer is greater")
else: 
	print("Float is greater")

# Practice declaring a method/function that requires no arguments
def Hello():
	print("Hello!")
Hello()

# Practice declaring a method/function with arguments
def Sum(a, b):
	method_return = a + b
	print(method_return)
Sum(test_integer,test_float)

# Practice using while loop
i = 0
while (i < 5):
	print("You are at increment " + str(i))
	i = i+1

# Practice using foreach loop
test_array2 = [0, 1, 2, 3, 4, 5]
test_sum = 0
for x in test_array2:
	test_sum = test_sum+x
	print(test_sum)
# Personal Note: Python doesn't declare an explicit end. Requires a line break as well as a left indent to declare end of loop
print(str(test_sum) + " from loop")