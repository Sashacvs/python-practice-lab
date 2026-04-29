import math

transactions = ["100", "-50", "200.5", "error", "0", "NaN", "300", "-20.5"]

total = 0
valid_count = 0
invalid_count = 0
integer_count = 0
float_count = 0

for item in transactions:
      try:
            item = item.strip()
            num = float(item)
            if math.isnan(num):
                  print(f"{item} is not a valid number")
                  invalid_count += 1
            elif num > 0:
                  valid_count +=1
                  print(item)
                  total = total + num
            else:
                  print(f"{item} is not a positive number")
                  invalid_count += 1
            if num.is_integer():
                        integer_count +=1
            else:
                        float_count +=1
      except ValueError:
            invalid_count += 1
            print(f"{item} is not a number")

print("The total transactions are",total)
print("Total Valid values are",valid_count)
print("Total invalid count is",invalid_count)

#Calculate and print the average amount
if valid_count !=0:
      average = total/valid_count
else:
      print("Average is not calculatable")

print("The average value is",average)

#Check for class of the average
if average > 200:
      print("High Value")
elif average > 100:
      print("Medium Value")
else:
      print("Low Value")


print("number of integers are",integer_count)
print("number of float counts are",float_count)