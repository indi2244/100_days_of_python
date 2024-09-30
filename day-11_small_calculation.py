year=int(input("Enter a year : "))

if (year % 4==0  and year % 100 !=0) or (year % 400 ==0):
    days=366 
else:
    days=365

seconds_in_a_day=24*60*60
seconds_in_a_year = seconds_in_a_day *days

print("total seconds in year", year , "is" ,seconds_in_a_year)



#using function

def isLeap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def seconds_in_year(year):
    if isLeap(year):
        days = 366
    else:
        days = 365

    seconds_in_a_day = 24 * 60 * 60
    seconds_in_a_year = seconds_in_a_day * days
    
    print(f"Total seconds in the year {year}: {seconds_in_a_year}")

year = int(input("enter a year : "))
seconds_in_year(year)

