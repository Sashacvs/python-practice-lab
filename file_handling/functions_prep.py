import math

def process_transactions(transactions):
    total = 0
    valid_count = 0
    invalid_count = 0
    integer_count = 0
    float_count = 0

    max_num = None
    min_num = None

    for item in transactions:
        item = item.strip()

        try:
            num = float(item)

            if math.isnan(num):
                print(f"{item} is not a valid number")
                invalid_count += 1

            elif num > 0:
                if num.is_integer():
                    print(int(num))
                    integer_count += 1
                else:
                    print(num)
                    float_count += 1

                valid_count += 1
                total += num

                if max_num is None or num > max_num:
                    max_num = num

                if min_num is None or num < min_num:
                    min_num = num

            else:
                print(f"{num:g} is not a positive number")
                invalid_count += 1

        except ValueError:
            print(f"{item} is not a number")
            invalid_count += 1

    return {
      "total": total,
      "valid_count": valid_count,
      "invalid_count": invalid_count,
      "integer_count": integer_count,
      "float_count": float_count,
      "max": max_num,
      "min": min_num
}


def analyze_transactions(total, valid_count):
    if valid_count == 0:
        return None, "NO VALID DATA"

    average = total / valid_count

    if average > 200:
        status = "HIGH VALUE"
    elif average > 100:
        status = "MEDIUM VALUE"
    else:
        status = "LOW VALUE"

    return average, status


def main():
    transactions = ["100", "-50", "200.5", "error", "0", "NaN", "300", "-20.5"]

    result = process_transactions(transactions)

    average, status = analyze_transactions(result["total"], result["valid_count"])

    print(result["total"])
    print(result["valid_count"])
    print(result["integer_count"])
    print(f"Integers: {result['integer_count']}")
    print(f"Floats: {result['float_count']}")
    print(f"Max: {result['max']:g}" if result['max'] is not None else "Max: None")
    print(f"Min: {result['min']:g}" if result['min'] is not None else "Min: None")

    if average is None:
        print("Average: Not calculatable")
    else:
        print(f"Average: {average}")

    print(f"Status: {status}")

    if result["invalid_count"] > 3:
       status = "FAIL"
    else:
      status = "PASS"


main()