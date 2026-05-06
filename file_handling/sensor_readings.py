import math
from unittest import result

def process_readings(readings):
    
    total = 0
    valid_count = 0
    invalid_count = 0
    integer_count = 0
    float_count = 0

    max_reading = None 
    min_reading = None

    for item in readings:
        item = item.strip()

        try:
            num = float(item)

            if math.isnan(num):
                print(f"{item} is not a valid number")
                invalid_count +=1
            elif 0<num<=80:
                if num.is_integer():
                    print(int(num))
                    integer_count+=1
                else:
                    print(num)
                    float_count+=1
                valid_count +=1
                total += num

                if max_reading is None or num > max_reading:
                    max_reading = num
                if min_reading is None or num < min_reading:
                    min_reading = num
            else:
                 print(f"{num:g} is not a positive integer")
                 invalid_count+=1
        except ValueError:
             print(f"{item} is not a valid number")
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
            "reason": reason

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

def main():
    readings = ["25", "30.5", "-10", "error", "45", "NaN", "60", "0", "85.2"]

    result = process_readings(readings)
    average, level = analyze_readings(result["total"], result["valid_count"])

    print(f"Total: {result['total']}")
    print(f"Valid count: {result['valid_count']}")
    print(f"Invalid count: {result['invalid_count']}")
    print(f"Integers: {result['integer_count']}")
    print(f"Floats: {result['float_count']}") 
    print(f"Max: {result['max']:g}" if result['max'] is not None else "Max: None")
    print(f"Min: {result['min']:g}" if result['min'] is not None else "Min: None")
    print(f"Test Status: {result['status']}")
    print(f"Reason: {result['reason']}")
    if average is None:
            print("Average: Not calculatable")
    else:
            print(f"Average: {average}")
            print(f"Level: {level}")

main()