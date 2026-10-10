# 1. Project Title
Student Performance Analytics System

**Author:** Sagar Santosh Yadav

# 2. Objective
The objective of this project is to build a Python-based Student Performance Analytics System that reads student data, processes and analyzes it using NumPy and Pandas, and produces meaningful academic results without relying on advanced machine learning. It solves the problem of manually calculating student metrics by automating the analysis of marks, grades, and class-wide performance trends.

# 3. Technologies Used
* **Python:** Core programming language for logic and loops.
* **NumPy:** Used for numerical calculations and computing averages.
* **Pandas:** Used for loading, organizing, and analyzing the dataset via DataFrames.

# 4. Dataset Description
The dataset (`students.csv`) consists of 20 realistic student records[cite: 2]. The key columns included are Student ID, Name, Department, Math_Marks, Science_Marks, English_Marks, and Attendance_Pct. 

# 5. Implementation
* **Step 1 - Data Loading:** Used Pandas `read_csv()` to ingest the student records and display basic information.
* **Step 2 - Data Processing:** Created reusable Python functions to calculate totals, compute averages using NumPy, and determine Pass/Fail status.
* **Step 3 - Data Application:** Used Pandas `.apply()` alongside custom functions and iteration loops to assign letter grades and passing status to each row.
* **Step 4 - Analysis:** Extracted overall class averages, subject-wise averages, and located the student with the highest average marks.

# 6. Key Features
* Calculates total marks and average marks for each individual student.
* Assigns grades (A, B, C, D, F) based on clearly defined average thresholds.
* Identifies pass/fail students based on a minimum passing mark condition.
* Generates subject-wise performance analysis to find the highest-performing subject.
* Identifies the top-performing student in the class.

# 7. Output/Screenshots
The final output is printed cleanly to the console. It displays:
* Overall Class Average
* Total Students Passed vs Total Students
* Best Performing Subject
* Top Performer details (Name, Average, Grade)
* A processed DataFrame preview containing the newly calculated columns.

<img width="363" height="331" alt="Screenshot 2026-10-10 115453" src="https://github.com/user-attachments/assets/f595739c-30c7-4388-a5a7-c69786d2937b" />
<img width="350" height="121" alt="Screenshot 2026-10-10 115508" src="https://github.com/user-attachments/assets/699e274d-436c-4faa-86e5-1d5e8149f644" />


# 8. Final Outcome
The project successfully achieved its goal of structuring and analyzing raw student data. It outputs a clear, understandable summary of class performance, proving that core Python data-analysis libraries can effectively automate academic reporting.

# 9. Challenges & Learning
* **Challenges:** Integrating NumPy mathematical operations seamlessly within Pandas DataFrame columns, and ensuring the Pass/Fail logic correctly iterated over only the subject columns without analyzing the ID or Attendance columns.
* **Learning:** Gained hands-on experience structuring a data analysis pipeline, using the Pandas `.apply()` method for row-wise operations, and organizing code into reusable functions for better readability. 

# 10. GitHub Repository
**Repository Link:** https://github.com/Sagaryadav2006/EWB_PYTHON_X_AI_ASSESMENT
