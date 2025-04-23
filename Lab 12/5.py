class Time:
	def __init__(self, hours=0, minutes=0, seconds=0):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds
		self.normalize()

	def normalize(self):
		if self.seconds >= 60:
			self.minutes += self.seconds // 60
			self.seconds %= 60
		if self.minutes >= 60:
			self.hours += self.minutes // 60
			self.minutes %= 60
		if self.hours >= 24:
			self.hours %= 24

	def __add__(self, other):
		seconds = self.to_seconds() + other.to_seconds()
		return Time.from_seconds(seconds)

	def __sub__(self, other):
		seconds = self.to_seconds() - other.to_seconds()
		return Time.from_seconds(seconds)

	def to_seconds(self):
		return self.hours * 3600 + self.minutes * 60 + self.seconds

	def from_seconds(seconds):
		hours = seconds // 3600
		seconds %= 3600
		minutes = seconds // 60
		seconds %= 60
		return Time(hours, minutes, seconds)

	def time_str(self):
		return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

time1 = Time(5, 45, 30)
time2 = Time(3, 20, 15)
print("Time 1:", time1.time_str())
print("Time 2:", time2.time_str())
result_add = time1 + time2
print("Addition of Time:", result_add.time_str())
result_sub = time1 - time2
print("Subtraction of Time:", result_sub.time_str())
