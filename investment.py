# Ask the user to enter investment amount and expected interest
# Each year their investment will increase by their investment + their investment * interest rate is
# Print out the earnings after 10 years

investment = int(input("Enter your investment amount: "))
interest = float(input("Enter your Expected interest: "))
interest = float(interest) * .01
for i in range(10):
    investment += investment * interest
print("year {} total balance = {:.2f}".format(i, investment))
