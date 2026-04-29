# 🐍 Python Practice Lab – Data Validation Script

## 📌 Overview

This project demonstrates practical Python skills by building a **data validation and processing script**.

The script reads input data from a file, validates and processes mixed numeric data (integers, floats, and edge cases), and generates meaningful output metrics such as total, count, average, and status classification.

---

## 🎯 Problem Statement

Given a file containing mixed data (valid integers, negative numbers, and invalid strings), the goal is to:

* Extract valid **positive numbers (integers and floats)**
* Ignore invalid entries (text, incorrect formats)
* Track:

  * Total sum
  * Valid count
  * Invalid count
* Compute:

  * Average
* Classify data as:

  * GOOD / BAD based on conditions
* Identify:

  * Maximum value
  * Minimum value

---

## 🧠 Key Concepts Used

* File Handling (`with open`)
* Data Cleaning (`.strip()`)
* Exception Handling (`try-except`)
* Conditional Logic (`if-else`)
* Looping (`for`)
* Aggregation (sum, count)
* Comparison Logic (max/min tracking)
* Formatted Output (`f-strings`)
* Floating-point handling (`float`)
* Special value handling (`math.isnan`)
* Type classification (`.is_integer()`)

---

## ⚙️ How It Works

1. Open the input file
2. Read each line and clean it
3. Attempt to convert the value to an integer and to a number using `float()`
4. If valid:

   * Check if positive
   * Add to total
   * Update counters
   * Track max and min
5. If invalid:

   * Handle using exception handling
6. Compute average safely
7. Print results and classification

---

## 🧪 Example Input

```
10
20
abc
-5
30
error
40
7.5
NaN
```

---

## 📊 Example Output

```
10
20
abc is not an integer
-5 is not a positive number
30
error is not an integer
40

Total: 100
Valid count: 4
Invalid count: 3
Average: 25.0
Status is GOOD
Max: 40
Min: 10
7.5
NaN is not a valid number
Integers: 4
Floats: 1
```

---  

## 🚀 How to Run

From project root:

```
python file_handling/numbers_analysis.py
```

Ensure the data file is located at:

```
data/numbers.txt
```

---

## 💡 Key Learnings

* Importance of handling unpredictable input data
* Difference between **validation (if-else)** and **error handling (try-except)**
* Writing safe and robust scripts that do not crash
* Building reusable patterns for real-world data processing
* Understanding file paths and project structure
* Understanding that successful numeric conversion does not always mean valid data (e.g., NaN)

## 🧠 Personal Takeaways

While building this, I initially struggled with handling invalid data and understanding when to use `if-else` vs `try-except`.

Debugging real errors (like failed integer conversions and file path issues) helped me understand how Python behaves in unpredictable situations.

This project helped me move from writing small snippets to thinking in terms of full workflows.

---

## 🔥 Next Improvements

* Export results to a file
* Add logging instead of print statements
* Accept user input dynamically

---

## 🧠 Author Note

This project is part of a structured Python learning approach focused on **practical problem-solving and real-world application**, rather than just syntax memorization.

## 📈 Learning Progress

This project is part of a structured Python learning journey focused on moving from fundamentals to real-world application.

### 🧩 Phase 1 – Foundations

* Variables and data types
* Strings and slicing
* Lists, tuples, sets, dictionaries
* Loops and conditional logic
* Functions and basic problem solving

### ⚙️ Phase 2 – Practical Python

* File handling (`with open`)
* Data cleaning using `.strip()`
* Exception handling (`try-except`)
* Understanding predictable vs unpredictable errors

### 🔄 Phase 3 – Applied Problem Solving

* Filtering valid vs invalid data
* Counting and aggregation (sum, frequency)
* Building reusable patterns (loop + condition + counters)
* Using f-strings for clean output

### 🚀 Phase 4 – Mini Project (Current)

* Built a complete data validation pipeline
* Handled real-world messy input scenarios
* Implemented safe processing logic
* Added metrics (total, count, average, max/min)
* Applied classification logic (GOOD / BAD)

### 🧠 Key Outcome

Moved from **learning syntax** to **building working logic for real-world scenarios**.

## 🧠 Approach to Building

The script was developed step-by-step:

1. First focused on reading and understanding file data
2. Introduced safe conversion using exception handling
3. Added validation logic for filtering valid entries
4. Built aggregation logic (sum, count, max, min)
5. Applied conditional logic for classification

This iterative approach helped in understanding not just *what works*, but *why it works*.

## Mini Projects

### Transaction Analyzer

This script processes a list of transaction values and performs:

- Validation of numeric inputs (handles errors and NaN values)
- Classification of valid vs invalid entries
- Filtering of positive transactions
- Calculation of:
  - Total transaction value
  - Average transaction value
- Categorization of average value (High / Medium / Low)
- Tracking of integer vs float inputs

### Example Handling
- "error" → invalid input
- "NaN" → not a valid number
- negative values → excluded from valid transactions

This project demonstrates:
- Exception handling (try-except)
- Data validation
- Conditional logic
- Basic data analysis patterns