x=float(input("enter first number"))
y=float(input("enter second number"))
add = x+y
print("addition is", add)
subtract= x-y
print("subtraction is", subtract)
mult=x*y
print("multiplication is ", mult)
divide=x/y
print("division is", divide)
modulus=x%y
print("modulus is", modulus)
squared=x**y
print("squared is", squared)
divisor=x//y
print("divisor is" , divisor)

bill=float(input("enter the total amount of bill:"))
people = int(input('entr the total number of people:'))
tip=int(input("enter the percentage of tip"))

tip_amount= (bill *tip)/100
total_bill= bill + tip_amount
amount_without_tip= bill/people
amount_with_tip=total_bill/people

print("total tip amount", tip_amount)
print("total bill",total_bill)
print("amount without tip" , amount_without_tip)
print("amount with tip", amount_with_tip)

