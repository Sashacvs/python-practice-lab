# 🐍 Sensor Data Validation & Reporting

## 📌 What this is

This started as a simple script to read numbers and process them.

But once I started handling real-world type inputs (invalid values, NaN, negatives, etc.), it naturally turned into something a bit more structured — closer to a small **data validation and reporting pipeline**.

---

## 🎯 What problem it solves

In real scenarios (logs, sensors, testing data), input is rarely clean.

You’ll see things like:

* valid numbers → `25`, `30.5`
* negatives → `-10`
* invalid values → `error`
* edge cases → `NaN`, `0`

This script handles that by:

* filtering usable data
* safely rejecting bad input
* tracking useful metrics
* generating a clean, readable report

---

## 🚀 What it does

* Reads data from multiple files
* Cleans and validates each value
* Handles:

  * invalid strings
  * `NaN`
  * negative / out-of-range values
* Tracks:

  * total sum
  * valid / invalid counts
  * integer vs float count
  * max and min values
* Calculates average
* Classifies results (Critical / Normal / Low)
* Generates a structured report
* Saves output to a file

---

## ⚙️ How it works (flow)

```text
Read → Process → Analyze → Report → Save
```

* `read_readings_from_file()` → reads input
* `process_readings()` → validates + processes data
* `analyze_readings()` → calculates average + level
* `main()` → runs everything across multiple files
* `write_report()` → saves final output

---

## 🧪 Example Input

```
25
30.5
-10
error
45
NaN
60
0
85.2
```

---

## 📊 Example Output

```
Processing file: data/sensor_readings.txt
----------------------------------------
25
30.5
-10 is out of valid range
error is not a valid number
45
NaN is not valid

Total: 160.5
Valid count: 4
Invalid count: 5
Integers: 3
Floats: 1
Max: 60
Min: 25
Test Status: FAIL
Reason: Too many invalid readings
Average: 40.125
Level: Normal
```

---

## 📁 Project Structure

```
mini_projects/
└── sensor_data_validation/
    ├── sensor_data_validation.py
    └── README.md

data/
output/
```

---

## ▶️ How to run

```bash
python mini_projects/sensor_data_validation/sensor_data_validation.py
```

---

## 🔥 What changed for me while building this

Earlier I was just writing small scripts that worked for clean inputs.

With this, I had to think a bit more about:

* what happens when the data is messy
* how to avoid crashes instead of fixing them later
* how to make output readable instead of just printing values

That’s where it started feeling less like a basic script and more like something structured.

---

## 🧠 Final note

This project is simple, but it helped me focus on:

* handling edge cases properly
* organizing code using functions
* separating logic from output

Not perfect, but definitely a step forward from where I started.

Still building on this.

---

## 🚀 Possible improvements

* Add logging instead of message list
* Export reports to CSV / JSON
* Add command-line input support
* Add basic unit tests
