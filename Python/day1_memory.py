# # textual data
# # strings

# message = "hello world"
# print(message)

# print(message[1])

# print(message[0:5])
# print(message[6:])

# greeting = "Hello"
# name = "John Doe name. yo"

# print(f"{greeting}, {name.upper}!")

# print("{},{} !.".format(greeting, name))

# # print(dir(greeting))

# print(help(str.splitlines))

# print(message.replace("hello", "You"))

# print(message.count("l"))
# print(message.find("lo"))
# print(name.upper())
# print(name.splitlines(keepends=True))

# ----------------------------------------------------------------------------------------------------------------

# # numeric data
# # integer
# # float

# num = 3
# num2 = 3.0

# print(num)
# print(num2)

# num += 7

# print(num)

# # Arithmetic operations
# print(num + num2)
# print(num - num2)
# print(round((num / num2), 3))
# print(num // num2)
# print(num * num2)
# print(num % num2)
# print(num ** num2)

# # Comparison operators
# print(num == num2)
# print(num != num2)
# print(num <= num2)
# print(num >= num2)
# print(num > num2)
# print(num < num2)
# print(num is num)


# # built in functions
# print(abs(-4))

# # type casting

# num_1 = '1000'

# print(num_1 * 10)

# num_1 = int(num_1)

# print(num_1 * 10)

# ----------------------------------------------------------------------------------------------------------------
# Conditional and booleans

age = 9

if age > 2 and age < 10:
    print("Kid")
elif age > 11 and age < 18:
    print("Teenager")
else:
    print("Adult")

# boolean operators

# and or not
a = "qwertyuiopas"
b = "qwertyuiopasdfghjkl"
print(a and b )
print(a or b)
# print(a not b)

condition = [False, None, 0, '', {}, (), []]

for i in condition:
    if i:
        print("True")
    else:
        print("False")

# object identtiy operator

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))

print(a == b)
print(a is b)


b = a
print(id(a))
print(id(a))

print(a == b)
print(a is b)
