#nested if ,elif

print("welcome to the rollercoster!")
print("what is your height in cm?")
height=int(input())

if(height>=120):
    print("you are allowed")
    print("please enter you age?")
    age=int(input())
    if age<12:
       print("you have to pay$5.")
    elif(age<=18):
      print("you have to pay $7.")
    else:
      print("please pay $12")

else:
    print("you are not alowed.")

#BMI calculator.
weight=float(input("enter your weight:"))
height=float(input("enter your height:"))
BMI=weight/(height*height)
print(f"your BMI is: ", {BMI})
if(BMI<18.5):
  print("you are underweight")
elif (BMI>=18.5 and BMI<25):
 print("your weight is normal.")
elif(BMI>=25 and BMI<30):
  print("you are slightly over weight.")
elif(BMI>=30 and BMI<35):
   print("you are slightly over weight.")
elif(BMI>35):
 print("you are obese.")
else:
  print("you are clinically obese.")


  #leap year
year= int(input("enter a year: "))
if(year %4==0):    #if the year is divisible by 4 then the next if will be checked.otherwise the last else will excute.
    if(year %100!=0):  #if the year is not divisible by 100 then the next if will be checked otherwise the second last else will excute.
      if(year %400==0):  #if it is also divisible by 400 then it is a leap year.
        print("it is a leap year")
      else:
        print("it is not a leap year.")
    else:
      print("it is not a leap year")
else:
    print("it is not a leap year")