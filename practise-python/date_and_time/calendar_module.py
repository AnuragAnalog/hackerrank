import datetime
date = input()
day_names= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
day_index = datetime.datetime.strptime(date, '%m %d %Y').weekday()
print(day_names[day_index].upper())
