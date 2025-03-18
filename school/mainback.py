import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')
django.setup()

from schoolbackend.models import *
import random

REGNO = None
ACCESSCODE = None

def faculties():
    UserFaculty.objects.create(faculty_name = "Faculty Of Engineering", description="For Engineering Students Only")
    UserFaculty.objects.create(faculty_name = "Faculty Of Computing", description="For Computer Science Students Only")
    UserFaculty.objects.create(faculty_name = "Faculty Of Arts", description="For Art and Management Students Only")
    UserFaculty.objects.create(faculty_name = "Faculty Of Science", description="For Biological and Physical Science Students Only")
    UserFaculty.objects.create(faculty_name = "Faculty Of Law", description="For Law Students Only")
    
def departments():
    UserDept.objects.create(dept_name = "Department of Agricultural Engineering", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Computer Engineering", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Civil Engineering", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Mechanical Engineering", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Food Engineering", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Chemical Engineering", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Electrical/Electronics Engineering", description = "For Agric Engineering Students")
    
    UserDept.objects.create(dept_name = "Department of Data Science", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Computer Science", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Cyber Security", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Information Technology", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Software Engineering", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Robotics and Embedded Systems", description = "For Agric Engineering Students")
    
    
    UserDept.objects.create(dept_name = "Department of Theatre Arts", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Music", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Accounting", description = "For Agric Engineering Students")
    
    UserDept.objects.create(dept_name = "Department of Mathematics", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Chemistry", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Physics", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of MicroBiology", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Animal and Environmental Biology", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Statistics", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Biochemistry", description = "For Agric Engineering Students")
    
    UserDept.objects.create(dept_name = "Department of Criminal Law", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Civil Law", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Constitutional Law Law", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Corporate/Business Law", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Cyber Law", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Tax Law", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of International Law", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Real Estate And Property Law", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Intellectual Property Law", description = "For Agric Engineering Students")
    UserDept.objects.create(dept_name = "Department of Environmental Law", description = "For Agric Engineering Students")
    
def courses():
    UserCourses.objects.create(course_name = "General Physics 1", course_code="PHY111")
    UserCourses.objects.create(course_name = " Physics II", course_code="PHY112")
    UserCourses.objects.create(course_name = "General Physics Practical", course_code="PHY117")
    UserCourses.objects.create(course_name = "General Mathematics", course_code="MTH111")
    UserCourses.objects.create(course_name = "Engineering Mathematics 1", course_code="MTH112")
    UserCourses.objects.create(course_name = "General Studies(Use-Of-English)", course_code="GST111")
    UserCourses.objects.create(course_name = "Discrete Maths For Computing", course_code="CPE113")
    UserCourses.objects.create(course_name = "General Chemistry", course_code="CHM111")
    UserCourses.objects.create(course_name = "General Chemistry Practical", course_code="CHM117")
    UserCourses.objects.create(course_name = "General Physics 1", course_code="PHY111")
    UserCourses.objects.create(course_name = "Use of English and Communication Studies", course_code="GST111")
    
    UserCourses.objects.create(course_name = "Intro To English Language Studies", course_code="ENG111")
    UserCourses.objects.create(course_name = "Intro To Literature", course_code="ENG112")
    UserCourses.objects.create(course_name = "African History to 1500", course_code="HIS111")
    UserCourses.objects.create(course_name = "African History from 1500", course_code="HIS112")
    UserCourses.objects.create(course_name = "Intro To Philosophy", course_code="PHI111")
    UserCourses.objects.create(course_name = "Logic and Critical Thinking", course_code="PHI112")
    UserCourses.objects.create(course_name = "Intro To Literary Studies", course_code="LIT111")
    UserCourses.objects.create(course_name = "African Literature", course_code="LIT112")
    UserCourses.objects.create(course_name = "Comparative Religion", course_code="REL111")
    UserCourses.objects.create(course_name = "Intro To Religious Studies", course_code="REL112")
    UserCourses.objects.create(course_name = "Use of English and Communication Studies", course_code="GST111")
    
    UserCourses.objects.create(course_name = "Fundamentals of Programming", course_code="CSC111")
    UserCourses.objects.create(course_name = "Digital Logic and Computer Organization", course_code="CSC112")
    UserCourses.objects.create(course_name = "Introduction to CyberSecurity", course_code="CSC113")
    UserCourses.objects.create(course_name = "Web Dev Fundamentals", course_code="CSC114")
    UserCourses.objects.create(course_name = "Calculus and Linear Algebra", course_code="MAT111")
    UserCourses.objects.create(course_name = "General Physics for Computing I", course_code="PHY111")
    UserCourses.objects.create(course_name = "General Physics for Computing II", course_code="PHY112")
    UserCourses.objects.create(course_name = "Use of English and Communication Studies", course_code="GST111")
    
    UserCourses.objects.create(course_name = "General Biology I", course_code="BIO111")
    UserCourses.objects.create(course_name = "General Biology II", course_code="BIO111")
    UserCourses.objects.create(course_name = "General Chemistry I", course_code="CHM111")
    UserCourses.objects.create(course_name = "General Chemistry II", course_code="CHM112")
    UserCourses.objects.create(course_name = "General Physics", course_code="PHY111")
    UserCourses.objects.create(course_name = "General practical physics", course_code="PHY117")
    UserCourses.objects.create(course_name = "General Mathematics I", course_code="MTH111")
    UserCourses.objects.create(course_name = "General Mathematics II", course_code="PHY112")
    UserCourses.objects.create(course_name = "Introduction to Computer Science", course_code="COS111")
    UserCourses.objects.create(course_name = "Introduction to Statistics", course_code="STA111")
    UserCourses.objects.create(course_name = "Use of English and Communication Studies", course_code="GST111")
    
    UserCourses.objects.create(course_name = "Introduction to Law", course_code="LAW111")
    UserCourses.objects.create(course_name = "Legal Method", course_code="LAW111")
    UserCourses.objects.create(course_name = "Nigerian Legal System I", course_code="LAW111")
    UserCourses.objects.create(course_name = "Nigerian Legal System II", course_code="LAW111")
    UserCourses.objects.create(course_name = "Constitutional Law I", course_code="LAW111")
    UserCourses.objects.create(course_name = "Constitutional Law II", course_code="LAW111")
    UserCourses.objects.create(course_name = "Legal Research and Writing", course_code="LAW111")
    UserCourses.objects.create(course_name = "Law and Society", course_code="LAW111")
    UserCourses.objects.create(course_name = "Use of English and Communication Studies", course_code="GST111")
    
def regno():
    global REGNO
    no = "0123456789"
    REGNO = "".join(random.choices(no, k=10))
    # return student_reg_no

def accesscode():
    global ACCESSCODE
    letters = "ABC0123456789"
    ACCESSCODE = "".join(random.choices(letters, k=5))
        
def create_student_account():
    global REGNO
    global ACCESSCODE
    student_name = input("Surname: ")
    o_name = input("Other Names: ")
    s_email = input("Email: ")
    # conditions for email
    if '.com' not in s_email:
        return
    else:
        home_address = input("House Address: ")
        student_dob = input("Date Of Birth: ")
        student_parent = input("Parent/Guardian Name: ")
        n_of_k = input("Next Of Kin: ")
        try:
            student_phone = int(input("Phone Number: "))
            parent_contact = int(input("Parent/Guardian Phone Number: "))
            n_of_k_contact = int(input("Next Of Kin Phone Number: "))
        except ValueError:
            print("Invalid Phone Number Details")
            
            # conditions for length of phone
        if len(str(student_phone)) != 11 and len(str(parent_contact)) != 11 and len(str(n_of_k_contact)) != 11:
            print("Phone Numbers MUst Be 11 Digits Long")
            return
        else:
            print("Account Created Successfully")
            regno()
            accesscode()
            print(f"Here's your Registration NNumber: {REGNO} \nAccess Code: {ACCESSCODE}")
            print("Login to complete the registration")
            
    sign_up = Student.objects.create(surname=student_name, other_names=o_name, reg_no=REGNO, access_code=ACCESSCODE, email=s_email, phone_number=student_phone, dob=student_dob, guardian=student_parent, guardian_contact=parent_contact, address=home_address, next_of_kin=n_of_k, n_o_k_contact=n_of_k_contact)
    sign_up.save()
# create_student_account()

def list_faculty():
    faculty = UserFaculty.objects.all()
    # iterate over the faculty to get a list of the faculties
    for index, faculties in enumerate(faculty):
        new_index = index + 1
        
        print(f"{new_index}. {faculties}")

def list_depts():
    dept = UserDept.objects.all()
    
    # iterate over to print the list of departments
    for index, depts in enumerate(dept):
        new_index = index + 1
        print(f"{new_index}. {depts}")
# list_depts()

def register():
    print("ONLINE SCREENING REGISTRATION PROCESS")
    
    # get the student
    student = Student.objects.get(reg_no=login_reg_no)
    
    faculty = UserFaculty.objects.all()
    # iterate over the faculty to get a list of the faculties
    for index, faculties in enumerate(faculty):
        new_index = index + 1
        
        print(f"{new_index}. {faculties}")
    
    # user choice of faculty
    faculty_choice = int(input("Enter Preferred Faculty Id: "))
    
    try:
        choice_faculty = UserFaculty.objects.get(id=faculty_choice)
    except UserFaculty.DoesNotExist:
        print("Invalid Faculty Id!")
        return
    
    usr_dept = UserDept.objects.filter(unique_key = choice_faculty)
    
    #iterate over the department list to get the list of departments
    for index, depts in enumerate(usr_dept):
        n_index = index + 1
        print(f"{n_index}. {depts}")
    
    department_choice = int(input("Enter Preferred Department Id: "))
    
    try:
        department_choice_choice = UserDept.objects.get(id=department_choice)
    except UserDept.DoesNotExist:
        print("Invalid Faculty Id!")
        return
    
    user_profile = StudentProfile.objects.create(student=f"{student.surname} {student.other_names}", bio=f"A {department_choice_choice.dept_name}", faculty=choice_faculty, department=department_choice_choice)


def studentlogin():
    """Login Function"""
    global login_reg_no
    login_reg_no = input("Enter your Reg No: ")
    login_access_code = input("Enter your Access Code: ")
    
    # check in database
    confirm_login = Student.objects.filter(reg_no=login_reg_no, access_code=login_access_code)
    student = Student.objects.get(reg_no = login_reg_no)
    # iterate over to check authenticity
    for user_details in confirm_login:
        if not confirm_login.exists():
            print("Access Denied")
            print("Create an Account Instead!")

        else:
            print(f"Login Successful \nWelcome {user_details.other_names} {user_details.surname}")
            choice = input("Enter 'y' to continue: ").upper()

def student_bio():
    pass
  
def register_courses():
    student = Student.objects.get(reg_no=login_reg_no)
    
    faculty = UserFaculty.objects.all()
    # iterate over the faculty to get a list of the faculties
    for index, faculties in enumerate(faculty):
        new_index = index + 1
        
        print(f"{new_index}. {faculties}")
    
    # user choice of faculty
    student_faculty = int(input("Enter your Faculty Id: "))
    
    try:
        choice_faculty = UserFaculty.objects.get(id=student_faculty)
    except UserFaculty.DoesNotExist:
        print("Invalid Faculty Id!")
        return
    
    usr_dept = UserDept.objects.filter(unique_key = choice_faculty)
    
    #iterate over the department list to get the list of departments
    for index, depts in enumerate(usr_dept):
        n_index = index + 1
        print(f"{n_index}. {depts}")
    
    student_department = int(input("Enter Preferred Department Id: "))
    
    try:
        department_choice_choice = UserDept.objects.get(id=student_department)
    except UserDept.DoesNotExist:
        print("Invalid Faculty Id!")
        return
    student_profile = StudentProfile.objects.filter(department=department_choice_choice)
    # usercourses = UserCourses.objects.get()
    # courseenrollment = CourseEnrollment.objects.
    
    usr_course = UserCourses.objects.filter(unique_key = choice_faculty)
    
    # iterate over the courses to get the list of courses
    for index, course in enumerate(usr_course):
        index_n = index + 1
        print(f"{index_n}. {course}")
    
    count = len(usr_course)
    while count != 0:
        course_no = int(input("Enter the Id for all the courses listed above: "))
        if course_no < 0 or course_no > len(usr_course):
            print("Invalid Course Id!")
            return
        else:
            selected_course = usr_course[course_no - 1]
            registered_course = CourseEnrollment.objects.create(student=student, course=selected_course)
            registered_course.save()
            print("Courses Registered Successfully!")
            count -= 1

# studentlogin()
# register_courses()


def update_bio():
    print("MAKE CHANGES TO YOUR BIO")
    login_reg_no = input("Enter your Reg No: ")
    login_access_code = input("Enter your Access Code: ")
    
    # check in database
    confirm_login = Student.objects.filter(reg_no=login_reg_no, access_code=login_access_code)

    # iterate over to check authenticity
    for user_details in confirm_login:
        if not confirm_login.exists():
            print("Access Denied!!")
            return
    
    student = Student.objects.first()
    print(f"Login Successful \nWelcome {student.other_names} {student.surname}")

    choice = input("Enter 'y' to continue: ")
    if choice != "y":
        return

    user = [student]

    for index, details in enumerate(user):
        print(f"{index} {details}")

# update_bio()


def check_profile():
    """Function to Update profile and courses"""
    login_reg_no = input("Enter your Reg No: ")
    login_access_code = input("Enter your Access Code: ")
    
    # check in database
    confirm_login = Student.objects.filter()
    student = Student.objects.get(reg_no = login_reg_no)
    # iterate over to check authenticity
    for user_details in confirm_login:
        if login_reg_no != user_details.reg_no and login_access_code != user_details.access_code:
            print("Access Denied")
            return
        else:
            print(f"Login Successful \nWelcome {user_details.other_names} {user_details.surname}")
            choice = input("Enter 'y' to continue: ").upper()
            
    student_id = Student.objects.get(reg_no=login_reg_no)
    
    # get it to display all the user data
    student = StudentProfile.objects.get(student=student_id)
    
    # student_courses = UserCourses.objects.filter(unique_key = student_id)
    
    print("PERSONAL DETAILS")
    print(f"Name: {student_id.surname}, {student_id.other_names}")
    print(f"Registration Number: {student_id.reg_no}")
    print(f"Email: {student_id.email}")
    print(f"Phone Number: {student_id.phone_number}")
    print(f"Date Of Birth: {student_id.dob}")
    print(f"Parent/Guardian Details: {student_id.guardian} \nGuardian Contact: {student_id.guardian_contact}")
    print(f"Next Of Kin Details: {student_id.next_of_kin} \nNext Of Kin Contact: {student_id.n_o_k_contact}")
    print(f"Account Created on: {student_id.created_at}")
    print("\n" * 3)
    print("ACADEMIC DETAILS")
    print(f"Faculty Enrolled: {student.faculty}")
    print(f"Department Enrolled: {student.department}")
    print(f"Screening Date: {student.created_on}")

check_profile()

def main():
    print("WELCOME TO COVENANT SCHOOLS")
    print("\n" * 3)

    account_choice = input("Login To Continue/Create Account \nEnter 'L' to LOGIN, 'C' to Create Account \n>>").upper()
    if account_choice != 'L' or account_choice != 'C':
        return
    if account_choice == "L":
        studentlogin()
    elif account_choice == "C":
        create_student_account()
    
# main()