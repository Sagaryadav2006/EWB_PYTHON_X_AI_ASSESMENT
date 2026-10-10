import pandas as pd
import numpy as np
from functions import calculate_totals_and_averages, assign_grades, check_pass_fail

try:
    df = pd.read_csv('students.csv')
    print("Dataset successfully loaded. Basic Information:\n")
    print(df.info())
except FileNotFoundError:
    print("Error: students.csv file not found.")
    exit()

subjects = ['Math_Marks', 'Science_Marks', 'English_Marks']

df = calculate_totals_and_averages(df, subjects)

df['Grade'] = df['Average_Marks'].apply(assign_grades)
df['Status'] = df.apply(lambda row: check_pass_fail(row, subjects), axis=1)

class_average = np.mean(df['Average_Marks'])
total_passed = len(df[df['Status'] == 'Pass'])
total_students = len(df)

subject_averages = {subject: np.mean(df[subject]) for subject in subjects}
best_subject = max(subject_averages, key=subject_averages.get)

top_student = df.loc[df['Average_Marks'].idxmax()]

print("\n--- Final Student Performance Analysis ---\n")
print(f"Overall Class Average: {class_average:.2f}")
print(f"Total Students Passed: {total_passed} out of {total_students}")
print(f"Best Performing Subject: {best_subject} (Average: {subject_averages[best_subject]:.2f})")
print(f"\nTop Performer:\nName: {top_student['Name']}, Average: {top_student['Average_Marks']:.2f}, Grade: {top_student['Grade']}")

print("\nProcessed Student Data:\n")
print(df[['Name', 'Total_Marks', 'Average_Marks', 'Grade', 'Status']].head())