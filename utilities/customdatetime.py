from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
custom_datetime = now.strftime("%Y-%m-%d %H-%M-%S")
print("date and time =", custom_datetime)