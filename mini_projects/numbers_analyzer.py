import math
data = ["12", "7.5", "error", "-3", "25", "18", "NaN", "40"]

total = 0
valid_count = 0
invalid_count = 0

max_num = None
min_num = None

integer_count = 0
float_count = 0

for item in data:
      try:
            item = item.strip()
            num = float(item)

            if math.isnan(num):
                  print(f"{item} is not a valid number")
                  invalid_count += 1

            elif num > 0:
                  if num.is_integer():
                        print(int(num))
                  else:
                        print(num)
                  valid_count += 1
                  total += num
                  if num.is_integer():
                        integer_count += 1
                  else:
                        float_count += 1

                  if max_num is None or num > max_num:
                        max_num = num

                  if min_num is None or num < min_num:
                        min_num = num

            else:
                  print(f"{int(num)} is not a positive number")
                  invalid_count += 1

      except ValueError:
            print(f"{item} is not a valid number")
            invalid_count += 1

print(f"Total: {total}")
print(f"Valid count: {valid_count}")
print(f"Invalid count: {invalid_count}")
print(f"Max: {max_num}")
print(f"Min: {min_num}")      
print(f"Integers: {integer_count}")
print(f"Floats: {float_count}")

  