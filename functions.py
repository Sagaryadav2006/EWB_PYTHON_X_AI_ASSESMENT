import numpy as np

def calculate_totals_and_averages(df, subject_columns):
    """Calculates total and average marks using Pandas and NumPy."""
    df['Total_Marks'] = df[subject_columns].sum(axis=1)
    df['Average_Marks'] = np.mean(df[subject_columns], axis=1)
    return df

def assign_grades(average):
    if average >= 90:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 40:
        return 'D'
    else:
        return 'F'

def check_pass_fail(row, subject_columns, passing_marks=40):
    for subject in subject_columns:
        if row[subject] < passing_marks:
            return 'Fail'
    return 'Pass'