total = 0
valid_count = 0
invalid_count = 0
max_num = None
min_num = None
with open ("data/numbers.txt", "r") as file:
      for line in file:
            line = line.strip()
            try:
                  num=int(line)
                  if num > 0:
                        print(num)
                        total += num
                        valid_count += 1
                        if max_num is None or num > max_num:
                              max_num = num
                        if min_num is None or num < min_num:
                              min_num = num
                  else:
                        print(f"{num} is not a positive number")
                        invalid_count += 1
            except ValueError:
                  print(f"{line} is not an integer")
                  invalid_count += 1
print(f"Total: {total}")
print(f"Valid count: {valid_count}")
print(f"Invalid count: {invalid_count}")
average = total / valid_count
if average > 15:
            print(f"Average: {average}")
            print("Status is GOOD")
else:
            print("Status is BAD")

print(f"Max: {max_num}")
print(f"Min: {min_num}")
