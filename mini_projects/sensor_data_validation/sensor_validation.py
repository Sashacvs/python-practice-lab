import math

def read_readings_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return []
def process_readings(readings):
    
    messages = []
    total = 0
    valid_count = 0
    invalid_count = 0
    integer_count = 0
    float_count = 0

    max_reading = None 
    min_reading = None

    for item in readings:

        try:
            num = float(item)

            if math.isnan(num):
                messages.append(f"{item} is not valid")
                invalid_count +=1
            elif 0<num<=80:
                if num.is_integer():
                    messages.append(str(int(num)))
                    integer_count+=1
                else:
                    messages.append(str(num))
                    float_count+=1
                valid_count +=1
                total += num

                if max_reading is None or num > max_reading:
                    max_reading = num
                if min_reading is None or num < min_reading:
                    min_reading = num
            else:
                 messages.append(f"{num:g} is not a positive integer or is not between limits mentioned")
                 invalid_count+=1
        except ValueError:
             messages.append(f"{item} is not a valid number")
             invalid_count+=1
    if invalid_count > 4:
            status = "FAIL"
            reason = "Too many invalid readings"
    else:
            status = "PASS"
            reason = "Readings within acceptable limits"

    return {
            "total": total,
            "valid_count": valid_count,
            "invalid_count": invalid_count,
            "integer_count": integer_count,
            "float_count": float_count,
            "max": max_reading,
            "min": min_reading,
            "status": status,
            "reason": reason,
            "messages": messages

}

def analyze_readings(total, valid_count):
      if valid_count == 0:
          return None, "NO VALID DATA"
      
      average = total/valid_count

      if average > 60:
          level = "Critical"
      elif average > 30:
          level = "Normal"
      else:
          level = "Low"

      return average, level
def write_report(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
def main():
   
   
   file_list = [
    "data/sensor_readings.txt",
    "data/practice.txt",
    "data/numbers.txt"
]
   full_report = "" # Where I begin to store the report for all files

   for file_path in file_list:
    #print(f"\nProcessing file: {file_path}")

    readings = read_readings_from_file(file_path)

    result = process_readings(readings)
    average, level = analyze_readings(result["total"], result["valid_count"])

    report = "" # Start of the report for the current file

    report += f"\nProcessing file: {file_path}\n"
    report += "-" * 40 + "\n"
    for msg in result["messages"]:
      report += msg + "\n"
    report += f"Total: {result['total']}\n"
    report += f"Valid count: {result['valid_count']}\n"
    report += f"Invalid count: {result['invalid_count']}\n"
    report += f"Integers: {result['integer_count']}\n"
    report += f"Floats: {result['float_count']}\n"

    report += f"Max: {result['max']:g}\n" if result['max'] is not None else "Max: None\n"
    report += f"Min: {result['min']:g}\n" if result['min'] is not None else "Min: None\n"

    report += f"Test Status: {result['status']}\n"
    report += f"Reason: {result['reason']}\n"


    if average is None:
            report += "Average: Not calculatable\n"
    else:
            report += f"Average: {average}\n"
            report += f"Level: {level}\n"

    print(report)  # optional

    full_report += report + "\n"   # 🔥 COLLECT

    # 🔥 AFTER LOOP
   write_report("output/report.txt", full_report)

#     print("-" * 40)
#     print(f"Total: {result['total']}")
#     print(f"Valid count: {result['valid_count']}")
#     print(f"Invalid count: {result['invalid_count']}")
#     print(f"Integers: {result['integer_count']}")
#     print(f"Floats: {result['float_count']}") 
#     print(f"Max: {result['max']:g}" if result['max'] is not None else "Max: None")
#     print(f"Min: {result['min']:g}" if result['min'] is not None else "Min: None")
#     print(f"Test Status: {result['status']}")
#     print(f"Reason: {result['reason']}")
#     if average is None:
#             print("Average: Not calculatable")
#     else:
#             print(f"Average: {average}")
#             print(f"Level: {level}") 

main()