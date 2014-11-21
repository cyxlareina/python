__author__ = 'lenovo'

from time import sleep

s_number=input("enter a number: ")

number=int(s_number)
print(number)

for number in range(1, 20):
      print(number)
      print ("Hello, world!")

      print ("Just", 20 - number, "more to go...")


print ("Hello, world")

print ("That was the last one... Phew!")

print("-----------------")

print("Please start cooking the spam. (I'll be backe in 3min)")

sleep(5)

print ("I'm baaack :)")


# How hot is hot enough?

hot_enough = 50


temperature = input("How hot is the spam?")

while int(temperature) < hot_enough :

      print ("Not hot enough... Cook it a bit more...")

      sleep(5)

      temperature = input("OK, How hot is it now?")

print ("It's hot enough - You're done!")
