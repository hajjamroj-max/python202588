import re
from functools import reduce

def name_validator(name):
    if re.match(r"^[a-zA-Z ]{3,30}$", name):  
        return True
    else:
        print("Warning: Invalid name!")
        return False

def family_validator(family):
    if re.match(r"^[a-zA-Z ]{3,30}$", family):  
        return True
    else:
        print("Warning: Invalid family name!")
        return False

def subject_validator(subject):  
    if re.match(r"^[\w ]{3,30}$", subject):  
        return True
    else:
        print("Warning: Invalid subject name!")
        return False

def score_validator(score):
    try:
        score_num = int(score)
        if 0 <= score_num <= 20:
            return True
        else:
            print("Warning: Score must be between 0 and 20!")
            return False
    except:
        print("Warning: Please enter a valid number!")
        return False

def show_menu():
    print("\n" + "="*25)
    print("  STUDENT SYSTEM")
    print("="*25)
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search by Age")
    print("4. Show by Subject")
    print("5. Show Averages")
    print("6. Exit")
    print("-"*25)
    choice = input("Choice: ")
    return choice

# تابع کمکی برای محاسبه معدل
def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

# تابع کمکی برای نمایش اطلاعات دانش‌آموز
def format_student_info(student):
    info = f"\n{student['name']} {student['family']} - {student['age']} years old\n"
    for j in range(3):
        info += f"   {student['subjects'][j]}: {student['scores'][j]}\n"
    total = sum(student['scores'])
    avg = total / 3
    info += f"   Average: {avg:.1f}"
    return info

# تابع کمکی برای فیلتر کردن بر اساس سن
def filter_by_age(age):
    def age_filter(student):
        return student['age'] == age
    return age_filter

# تابع کمکی برای فیلتر کردن بر اساس موضوع
def filter_by_subject(subject):
    def subject_filter(student):
        return subject in student['subjects']
    return subject_filter

# تابع کمکی برای جمع‌زدن
def sum_scores(total, student):
    return total + sum(student['scores'])

def show_students(students):
    if len(students) == 0:
        print("\nNo students available!")
        return
        
    print("\n--- All Students ---")
    # استفاده از map برای فرمت کردن اطلاعات دانش‌آموزان
    student_info_list = list(map(format_student_info, students))
    
    # نمایش بدون استفاده از enumerate
    counter = 1
    for info in student_info_list:
        print(f"{counter}. {info}")
        counter += 1

def show_averages(students):
    if len(students) == 0:
        print("\nNo students available!")
        return
        
    # استفاده از map برای محاسبه معدل هر دانش‌آموز
    def get_student_avg(student):
        total = 0
        for score in student['scores']:
            total += score
        avg = total / 3
        status = "PASS" if avg >= 10 else "FAIL"
        return {
            'name': f"{student['name']} {student['family']}",
            'avg': avg,
            'status': status
        }
    
    averages_list = list(map(get_student_avg, students))
    
    # استفاده از sorted برای مرتب‌سازی
    def sort_by_avg(item):
        return item['avg']
    
    sorted_averages = sorted(averages_list, key=sort_by_avg, reverse=True)
    
    # نمایش نتایج بدون استفاده از enumerate
    print("\nRank  Name  Average Status")
    print("-" * 40)
    
    counter = 1
    for item in sorted_averages:
        print(f"{counter:<5} {item['name']:<20} {item['avg']:<7.1f} {item['status']}")
        counter += 1

def show_by_subject(students):
    if len(students) == 0:
        print("\nNo students available!")
        return
        
    # جمع‌آوری تمام دروس
    all_subjects = []
    for student in students:
        for subject in student['subjects']:
            if subject not in all_subjects:
                all_subjects.append(subject)
    
    print("\nAvailable Subjects:")
    # نمایش بدون استفاده از enumerate
    counter = 1
    for subject in all_subjects:
        print(f"{counter}. {subject}")
        counter += 1
    
    try:
        choice = int(input("Select a subject: "))
        if choice < 1 or choice > len(all_subjects):
            print("Invalid selection!")
            return
        selected_subject = all_subjects[choice-1]
    except:
        print("Please enter a valid number!")
        return
    
    # استفاده از filter برای پیدا کردن دانش‌آموزان با درس انتخاب شده
    filtered_students = list(filter(filter_by_subject(selected_subject), students))
    
    # پیدا کردن نمره مربوط به درس برای هر دانش‌آموز
    student_scores = []
    for student in filtered_students:
        for i in range(3):
            if student['subjects'][i] == selected_subject:
                student_scores.append({
                    'name': f"{student['name']} {student['family']}",
                    'age': student['age'],
                    'score': student['scores'][i]
                })
                break
    
    # استفاده از sorted برای مرتب‌سازی بر اساس نمره
    def sort_by_score(item):
        return item['score']
    
    sorted_students = sorted(student_scores, key=sort_by_score, reverse=True)
    
    print(f"\n--- Students in {selected_subject} ---")
    # نمایش بدون استفاده از enumerate
    counter = 1
    for student in sorted_students:
        print(f"{counter}. {student['name']} ({student['age']} years old) - Score: {student['score']}")
        counter += 1

def search_age(students):
    if len(students) == 0:
        print("\nNo students available!")
        return
        
    try:
        search_age = int(input("Enter age to search: "))
    except:
        print("Please enter a valid age!")
        return
        
    # استفاده از filter برای پیدا کردن دانش‌آموزان با سن مورد نظر
    filtered_students = list(filter(filter_by_age(search_age), students))
    
    if not filtered_students:
        print(f"No students found with age {search_age}")
        return
        
    print(f"\n--- Students with age {search_age} ---")
    # استفاده از map برای نمایش اطلاعات دانش‌آموزان
    student_info_list = list(map(format_student_info, filtered_students))
    
    # نمایش بدون استفاده از enumerate
    counter = 1
    for info in student_info_list:
        print(f"{counter}. {info}")
        counter += 1