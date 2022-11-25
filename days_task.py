from datetime import date,timedelta

val = int(input("Enter the no. of working days : "))

day_before = date.today() - timedelta(days=1)
weekands = 0
working_day = 0
for rec_date in range(val): 
	current = day_before - timedelta(days=rec_date)
	print("============>>>", current)
	print("============>>>", current.weekday())
	if current.weekday() == 5 or current.weekday() == 6:
		weekands +=1
	else:
		working_day+=1

print("==============>>>>", working_day)
print("==============>>>>", weekands)
val+=weekands

for rec in range(val):
	current_date = day_before - timedelta(days=rec_date)

print("===================>>>>>", current_date)


# no_of_days = working_day + weekands



