# EXE 2 - Good morning SIR
import time

t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))
print(hour)

if (hour > 0 and hour < 12):
    print("Good Moring Sir!")
if (hour >= 12 and hour < 17):
    print("Good Afternoon Sir!")
if (hour >= 17 and hour <= 24):
    print("Good night Sir!")
else:
    print("Wrong input")
