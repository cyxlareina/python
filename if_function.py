__author__ = 'lenovo'

print ("Welcome to the Area calculation program")

print ("---------------------------------------")

print()


# Print out the menu:

print ("Please select a shape:")

print ("1 Rectangle")

print ("2 Circle")

print("3 Square")


#Get the user's choice:

s_shape = input(">; ")

shape=int(s_shape)
#Calculate the area:

if shape == 1:

      height = input("Please enter the height: ")

      width = input("Please enter the width: ")

      area = int(height) *int(width)

      print ("The area is ", area)

elif shape ==2:

      radius = input("Please enter the radius: ")

      area = 3.14 * (int(radius)**2)

      print ("The area is ", area)
elif shape==3:
     edge=input("Please enter the edge length: ")

     area=int(edge)*int(edge)
     print ("The area is ", area)

else:
    print("kidding")