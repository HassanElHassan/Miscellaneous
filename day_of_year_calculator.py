def is_year_leap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return None
    lst = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2:
        if is_year_leap(year):
            return lst[month-1] + 1
        else:
            return lst[month-1]
    else:
        return lst[month-1]
        

def day_of_year(year, month, day):
    if month > 12 or month < 1:
        return None
        
    if day > days_in_month(year, month):
        return None
    
    days = 0
    for i in range(month-1):
        days+= days_in_month(year, i+1)
    days+=day
    return days

  
# Test
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 3, 1, 11]
test_day = [15, 28, 8, 35]
test_results = [46, 88, 8, None]
print("year", "month", "day", " -> ", "expected result", " - ", "result", " -> ", "test outcome"  )
for i in range(len(test_years)):
	year = test_years[i]
	month = test_months[i]
	day = test_day[i]
	print(year, month, day, "->",test_results[i], " - ", end="")
	result = day_of_year(year, month, day)
	if result == test_results[i]:
		print(result," -> ", "OK")
	else:
		print(result," -> ", "Failed")
