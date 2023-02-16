import datetime

print("Yesterday was:", (datetime.datetime.now() - datetime.timedelta(1)).strftime("%Y-%m-%d"))
print("Today is:", datetime.datetime.now().strftime("%Y-%m-%d"))
print("Tomorrow will be:", (datetime.datetime.now() + datetime.timedelta(1)).strftime("%Y-%m-%d"))
