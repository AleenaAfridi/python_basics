 
print("welcome to the rollercoster!")
print("what is your height in cm?")
height=int(input())

if(height>=120):
    print("you are allowed")
    print("please enter you age?")
    age=int(input())
    if age<12:
       bill=5
       print("you have to pay$5.")
       
    elif(age<=18):
      bill=7
      print("you have to pay $7.")
    elif(age>=45 and age<=55):
      bill=0
      print("you will get free tickets.")
    else:
      bill=12
      print("please pay $12")
    photo=input("do you want a photo y-yes, n-no:")
  
    if(photo=="y"):
     bill+=3
     print(f"your total bill is{bill}")
    else:
      print(f"your total bill is {bill}" )

else:
    print("you are not alowed.")

#pizza task:

pizza=input("which size do you want to order s-small, m-medium, l-large?")
 
if(pizza=="s"):
 bill=15
elif(pizza=="m"):
  bill=20
elif(pizza=="l"):
  bill=25

pepronni=input("do you want to add pepronni? y-yes, n-no")
if(pepronni=="y" and pizza=="s"):
 bill+=2
elif(pepronni=="y" and pizza=="m" or pizza=="l"):
  bill+=3
else:
  print(f"your total bill is: ${bill}")

cheese=input("do you want to add cheese? y or n")
if(cheese=="y"):
 bill+=1
 print(f"your total bill is:${bill}")
else:
  print(f"your total bill is: {bill}")

#love percentage task.
name1=input("enter the first name: ")
name2=input("enter the second name: ")
fullname=print(name1+name2)
lowername=fullname

t=lowername.count("t")
r=lowername.count("r")
u=lowername.count("u")
e=lowername.count("e")
first=t+r+u+e

l=lowername.count("l")
o=lowername.count("o")
v=lowername.count("v")
e=lowername.count("e")
second=l+o+v+e
print(str(first+second))

 
 


 



 

 