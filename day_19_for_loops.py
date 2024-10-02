for i in range(7):
    print(i)
for x in range (10):
    x="indira"
    print(x)

for days in range(7):
    print("day", days)

for months in range(12):
    print("month ", months+1)


loan = 1000
apr = 0.05
for i in range(10):
  loan+=(loan*apr)
  print("Year", i+1, "is", round(loan,2))