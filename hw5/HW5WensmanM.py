"""
 Author: Malik Wensman
 Email: mdwensma@ncsu.edu
 Class: CSC 251-001 Fall 2026
 Program: HW5
 Purpose: Reads student records (name, ID, grade) from an input file,
     sorts students by grade in descending order, and displays a
     formatted table along with exam statistics (min, max, mean, median).
 Bugs: None
 Acknowledgements: None
"""

import hw5_table_header as table_header
import math

def load_info(filename) -> list:
    """
    Reads student records from a file and returns them as a list of tuples.
    Each record consists of three consecutive lines: name, student ID, and grade.
    Grades outside the range (0, 110] are stored as None. If a student ID
    already exists in the list, their record is updated rather than duplicated.

    Parameters:
        filename (str): path to the input file containing student records

    Returns:
        students (list): list of (id, name, grade) tuples; grade is float or None
    """
    students = list()
    try:
        with open(filename, "r") as file:
            name_line = file.readline()
            while name_line != "":
                id_line   = file.readline()
                grade_line = file.readline()

                name = name_line.strip()
                if len(name) > 19:
                    name = name[:19]

                id = id_line.strip()
                if len(id) > 7:
                    id = id[:7]

                grade = float(grade_line.strip())   # raises ValueError if blank/missing
                if grade <= 0 or grade > 110:
                    grade = None

                # update existing student or append new one
                existing = -1
                for i, s in enumerate(students):
                    if s[0] == id:
                        existing = i
                        break
                if existing >= 0:
                    students[existing] = (id, name, grade)
                else:
                    students.append((id, name, grade))

                name_line = file.readline()
    except IOError as err:
        raise err
    except ValueError as err:
        print(f"Exception thrown: {err}")
        return students
    except Exception as err:
        print(f"Exception thrown: {err}")
        return students
    else:
        return students
    
def sort_info(students: list) -> list:
    """
    Sorts a list of student tuples by grade in descending order.
    Students with a None grade are placed at the bottom of the list.
    The sort is stable, so students with equal grades keep their original order.

    Parameters:
        students (list): list of (id, name, grade) tuples; grade is float or None

    Returns:
        sorted_students (list): new list of (id, name, grade) tuples sorted by
            grade descending, with None grades last
    """
    # sort by grade (index 2) in descending order
    # None grades sort to the bottom (treated as -inf)
    # students with the same grade stay in original order (stable sort)
    return sorted(students, key=lambda x: x[2] if x[2] is not None else -float('inf'), reverse=True)

def get_mean(students: list) -> float:
    """
    Calculates the arithmetic mean of all valid (non-None) student grades.

    Parameters:
        students (list): list of (id, name, grade) tuples; grade is float or None

    Returns:
        mean (float): average of all valid grades
    """
    valid = [s[2] for s in students if s[2] is not None]
    return sum(valid) / len(valid)

def get_median(students: list) -> float:
    """
    Calculates the median grade of all valid (non-None) student grades.
    For an even number of valid grades the median is the average of the
    two middle values; for an odd count it is the single middle value.

    Parameters:
        students (list): list of (id, name, grade) tuples; grade is float or None

    Returns:
        median (float): median of all valid grades
    """
    # remove N/A values and sort ascending
    grades = sorted(s[2] for s in students if s[2] is not None)
    n = len(grades)
    if n % 2 == 0:   # even count: average the two middle values
        return (grades[n // 2 - 1] + grades[n // 2]) / 2
    else:            # odd count: return the middle value
        return grades[n // 2]

def print_info(students: list):
    """
    Prints a formatted table row for each student showing their name,
    student ID, and grade. Grades are rounded up to the nearest whole
    number; a None grade is displayed as \"N/A\".

    Parameters:
        students (list): list of (id, name, grade) tuples; grade is float or None

    Returns:
        None
    """
    # print grade == None as "N/A"
    # print grade to nearest whole number. if float round to nearest whole number
    
    for student in students:
        id = str(student[0])
        name = student[1]
        if len(name) > 19:
            name = name[:19]

        grade = student[2]
        if grade is None:
            grade = "N/A"
        else:
            grade = math.ceil(grade)
        grade = str(grade)
        
        print(f"{name:<{20}}{id:>{7}}{grade:>8}")


def main():
    """
    Entry point for the program. Prompts the user for an input filename,
    loads and sorts student records, then prints a formatted grade table
    followed by exam statistics (minimum, maximum, mean, and median).
    Re-prompts on an IOError; exits on any other exception.

    Parameters:
        None

    Returns:
        None
    """
    while True:
        try:
            filename = input("Enter input filename: ")
            print(filename)

            student_dict = load_info(filename)

            sorted_students = sort_info(student_dict)

            mean = get_mean(student_dict)

            median = get_median(sorted_students)

            # print
            table_header.hw5_table_header()

            print_info(sorted_students)

            # get min/max from valid (non-N/A) grades only
            valid_grades = [s[2] for s in sorted_students if s[2] is not None]
            grade_max = valid_grades[0]   # highest (list is sorted descending)
            grade_min = valid_grades[-1]  # lowest
            
            print("\nExam Stats")
            print("-"*35)
            print(f"Minimum{int(grade_min):>28}")
            print(f"Maximum{int(grade_max):>28}")
            print(f"Mean{mean:>31.1f}")
            print(f"Median{median:>29.1f}")

            break
        except IOError as err:
            print(f"IOError Exception thrown: {err}.")
        except Exception as err:
            print(f"Exception thrown: {err}.")
            break 
    
        
if __name__ == "__main__":
    main()