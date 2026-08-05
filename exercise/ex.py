print("Hello, World!")

asp = 5
bsp = 15
sum = asp+bsp
print(sum)


x =5
y = 3.5
z = "Hello"
print(type(x))
print(type(y))
print(type(z)) 
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10))


x =1
a = float(x)
b = str(x)


print(type(a))
print(type(b))
print(type(x))

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
else:
  print("No, 'free' is not present.")


txt = "The best things in life are expensive!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[2:6])

a = "Hello, World!"
print(a.upper())

a = " Hello, World! "
print(a.strip()) 

a = "Hello"
b = "World"
c = a +" "+ b
print(c)



age = 36
#This will produce an error:
txt = f"My name is John, I am {age}" 
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = f"The price is {20 * 59} dollars"
print(txt)


txt = "We are the so-called \"Vikings\" from the north."

print(txt)

txt = "This will insert one \\ (backslash)."
print(txt) 

txt  = "Hello Hello, World!"

a = txt[2:5]
print(a.upper())
name = "Python"
print(f"I love {name}")

print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


def myFunction() :
  return False

if myFunction():
  print("YES!")
else:
  print("NO!")


x = "200"
print(isinstance(x, int))

print(10 > 9)
print(10 == 9)
print(bool("Hello"))
print(bool(0))
print(10+5)


sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

print(sum3)

x =2
y =3
print(x **y)

x = 15
y = 2

print(x // y)


numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")


num = 5
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)



x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


fruits = ["apple", "banana", "cherry"]

print("banana"  in fruits)

a =15
b = 4

print(a%b)
print(a//b)
print(a**b)
a+=10
print(a)


mylist = ["apple", "banana", "cherry"]

print(mylist[-3])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print(thislist[2:])

print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
thislist.sort()
print(thislist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


fruits = ['apple', 'banana', 'cherry']

x = fruits.count('apple')

print(x)


x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)


x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)


x = {"apple","babar", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"babar", "microsoft", "apple"}

zz = x.difference(y,z)
print(zz)


a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}

myset = a - b - c

print(myset)


colors = {"red", "green", "blue"}
colors.pop()
print(colors)


student = {
    "name": "Ali",
    "age": 22,
    "city": "Lahore"
}

print(student.get("name"))
print(student.get("email"))
student["email"] = "ali@gmail.com"
print(student.items())

print(student.items())

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(len(fruits))

(a,b,c) = ("apple", "banana", "cherry")
print(a)
print(b)
print(c)

import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x, y)

plt.show()


import seaborn as sns
import pandas as pd

df = pd.DataFrame({
    "x":[1,2,3,4],
    "y":[10,20,15,30]
})

sns.lineplot(data=df, x="x", y="y")