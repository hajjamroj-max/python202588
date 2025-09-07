# سیستم دانش‌آموز ساده
from datetime import datetime
from student_validations_functions import *

students = []

def add_student():
    print("\n--- Add Student ---")
    
    name = input("Name: ")
    family = input("Family: ")
    
    # تاریخ تولد و محاسبه سن
    year = int(input("Birth year: "))
    month = int(input("Birth month: "))
    day = int(input("Birth day: "))
    age = datetime.now().year - year
    
    # 3 درس و نمره
    subjects = []
    scores = []
    
    for i in range(3):
        subject = input(f"Subject {i+1}: ")
        score = int(input(f"Score {i+1}: "))
        subjects.append(subject)
        scores.append(score)
    
    # ذخیره
    student = {
        'name': name,
        'family': family,
        'age': age,
        'year': year,
        'month': month,
        'day': day,
        'subjects': subjects,
        'scores': scores
    }
    
    students.append(student)
    print(f"{name} {family} added!")

while True:
    option = show_menu()
    
    if option == "1":
        add_student()
    elif option == "2":
        show_students(students) 
    elif option == "3":
        search_age(students)  
    elif option == "4":
        show_by_subject(students)  
    elif option == "5":
        show_averages(students)  
    elif option == "6":
        break
    else:
        print("Invalid!")
    
    input("Enter...")