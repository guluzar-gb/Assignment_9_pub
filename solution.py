#Task1
name=input("enter your name: ").lower()
name_2="guluzar"
if name == name_2:
    print(f"Hello, {name_2}! The password is : W@12")
else:
   print(f"Hello, {name}! See you later.")      

#TASK2
age = bool(int(input("Are you a cigarette addict older than 75 years old? (Yes:1, No:0)")))
chronic = bool(int(input("Do you have a severe chronic disease? (Yes:1 / No:0) :")))
immune = bool(int(input("Is your immune system too weak? (Yes:1 / No:0) : ")))

if (age or chronic or immune) is True:
    print("You are in risky group")
else:
   print("You are not in risky group")

#TASK3
year = int(input("enter a four-digit year:"))
if (year % 4==0 and (year % 100 != 0 or year % 400 == 0)):
    print("it is a leap year")
else:
    print("it is not a leap year")