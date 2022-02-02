numDays = int(input("How many day's temperature? "))
total = 0
temp = []
for i in range(0, numDays):
    nextDay = int(input("Day" + str(i + 1) + "'s high temp: " ))
    temp.append(nextDay)
    total += temp[i]
    
avg = round(total/numDays, 2)
print("\nAverage = " + str(avg)) # converted to string to for concatenation
above = 0
for i in temp:
    if i > avg:
        above += 1
    

print(str(above) + "day(s) are above avrage")