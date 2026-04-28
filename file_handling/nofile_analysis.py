data = ["10", "20", "abc", "-5", "30", "error", "40"]

total = 0
valid_count = 0
invalid_count = 0

max_num = None
min_num = None

for item in data:
    try:
        item = item.strip()
        num = int(item)
        if num > 0:
             print(num)
             valid_count += 1
             total += num
             if max_num is None or num>max_num:
                  max_num = num
             if min_num is None or num<min_num:
                   min_num = num
        else:
                  print(f"{num} is not a positive number")
                  invalid_count += 1
    except ValueError:
            print(f"{item} is not an integer")
            invalid_count += 1
print(f"Total: {total}")
print(f"Valid count: {valid_count}")
print(f"Invalid count: {invalid_count}")
if valid_count == 0:
    print("No valid numbers found")
else:
    average = total / valid_count
    print(f"Average: {average}")

    if average > 25:
        print("Status is EXCELLENT")
    elif average > 15:
        print("Status is GOOD")
    else:
        print("Status is BAD")