import os
import math
import json
import sys

def read_readings_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-16", errors="ignore") as file:
            data = [line.strip() for line in file if line.strip()]
        print(f"Debug: raw data from {file_path}: {repr(data)}")
        return data
    except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return []
def process_readings(readings, config):
    
    messages = []
    total = 0
    valid_count = 0
    invalid_count = 0
    integer_count = 0
    float_count = 0

    max_reading = None 
    min_reading = None
    min_limit = config.get("min_value", 0)
    max_limit = config.get("max_value", 100)
    for item in readings:

        try:
            num = float(item)

            if math.isnan(num):
                messages.append(f"{item} is not valid")
                invalid_count +=1
            elif min_limit < num <= max_limit:
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
    limit = config.get("max_invalid", 4)  # Default to 4 if not specified
    if invalid_count > limit:
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

def analyze_readings(total, valid_count, config):

      crit_limit = config.get("critical_threshold", 60)  # Default to 60 if not specified
      avg_limit = config.get("average_threshold", 30)  # Default to 30 if not specified

      if valid_count == 0:
          return None, "NO VALID DATA"
      
      average = total/valid_count

      if average > crit_limit:
            level = "Critical"
      # if average > 60:
      #     level = "Critical"
      elif average > avg_limit:
           level = "Normal"
      else:
           level = "Low"

      return average, level
def write_report(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
def main():

    total_files = 0
    passed_files = 0
    failed_files = 0

    file_list = ["data/sensor_readings.txt", "data/numbers.txt", "data/practice.txt"]
    config_file = "settings.json"
# 2. DYNAMIC CLI LOGIC (The Upgrade)
    if len(sys.argv) > 1:
        target = sys.argv[1] # user types a folder or a file
    else:
        target = "data/"    # Our default warehouse
    
    #The fork in the road: Is it a file or a folder?
    if os.path.isdir(target):
         print(f"Automated Scan: Looking inside folder '{target}'...")
         file_list = []

         #Look at every single item inside the folder
         for item in os.listdir(target):
              if item.endswith(".txt"): # Only care about .txt files such is the industry standard
                   full_path = os.path.join(target, item)
                   file_list.append(full_path)
    else: 
         file_list = [target] # Just one file to process

# Handle the JSON config (always the last argument if provided)
    config_file = "settings.json"
    if len(sys.argv) > 2:
        config_file = sys.argv[-1]

    try:
        with open(config_file, "r") as file:
            config = json.load(file)
    except FileNotFoundError:
        print(f"Error: Config file '{config_file}' not found!")
        return
   
#    # The Rulebook
#    config = {
#             "min_val": 0,
#             "max_val": 80,
#             "max_invalid": 0,
#             "critical_threshold": 60,
#             "average_threshold": 30
#       }
    full_report = "" # Where I begin to store the report for all files

    for file_path in file_list:
    #print(f"\nProcessing file: {file_path}")

        readings = read_readings_from_file(file_path)

        result = process_readings(readings,config)
        total_files += 1
        if result["status"] == "PASS":
            passed_files += 1

        average, level = analyze_readings(result["total"], result["valid_count"], config)

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
                report += "Level: N/A\n" # Added for consistency
        else:
                report += f"Average: {average}\n"
                report += f"Level: {level}\n"

        print(report)  # optional

        full_report += report + "\n"   # 🔥 COLLECT

    # 🔥 AFTER LOOP
   
    write_report("output/report.txt", full_report)
    print("\n" + "="*40)
    print("       FINAL EXECUTION SUMMARY")
    print("="*40)
    if total_files > 0:
        fail_files = total_files - passed_files
        pass_rate = (passed_files/total_files) * 100
        print(f"Total files processed: {total_files}")
        print(f"Passed files: {passed_files}")
        print(f"Failed files: {fail_files}")
        print(f"Pass Rate:  {pass_rate:.1f}%")
        
    else: 
        print("No files processed. Pass Rate: N/A")
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