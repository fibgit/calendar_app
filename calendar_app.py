import calendar

c = calendar.TextCalendar(calendar.MONDAY)

print("Welcome to my Calendar application")

y = int(input("Please enter any year: "))
m = int(input("Please enter any month number: "))

str = c.formatmonth(y,m)

print(str)

print("Have a great day!.")