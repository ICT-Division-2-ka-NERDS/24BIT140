class Date:
	def __init__(self, day, month, year):
		self.day = day
		self.month = month
		self.year = year
	def __eq__(self, other):
		return self.day == other.day and self.month == other.month and self.year == other.year
	def date_str(self):
		return str(self.day) + "/" + str(self.month) + "/" + str(self.year)

date1 = Date(15, 8, 2025)
date2 = Date(15, 8, 2025)
date3 = Date(10, 5, 2023)

print("Date 1:", date1.date_str())
print("Date 2:", date2.date_str())
print("Date 3:", date3.date_str())

# Comparing dates
print("Date 1 equal to Date 2?:", date1 == date2)  
print("Date 1 equal to Date 3?:", date1 == date3)  
