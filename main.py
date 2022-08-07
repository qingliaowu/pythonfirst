
import random

a = random.random()

print(a)
print("Hello World")


day = 21
month = 'Oct'
temp = 65

x = f"Today is {day}"

print (x)


a = True

a = False

if a:
  print("ok")
else:
  print("ng")


print("------------------")


a = [3,4]
length = len(a)

print(length)
a.append(5)
b = a
print(b)

del(b[0])

for number in range(10):
  print (number, end =" ")
