# prompt users to enter their age
age = eval(input("How old are you ? "))
# Check if user is upto 5yrs old if true then place the user in kindergarten
if age < 5:
    print("You are not old enough")
elif age == 5:
    print("Go to kindergarten")
# Check if user is over 5yrs old if true then place the user in grade 1 - 12
elif age > 5 and age <= 17:
    grade = age - 5
    print("go to grade {}".format(grade))
# Check if user is over 17yrs old if true then the user should go to college
else:
    print("Go to college")
