from django.db import models

# Create your models here.
class Student(models.Model):
    surname = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255, null=True)
    reg_no = models.CharField(max_length=25)
    access_code = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    dob = models.CharField(max_length=50)
    guardian = models.CharField(max_length=255, null=True, blank=True)
    guardian_contact = models.CharField(max_length=25)
    address = models.CharField(max_length=255, null=True)
    next_of_kin = models.CharField(max_length=255)
    n_o_k_contact = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.surname}, {self.other_names} -- {self.reg_no}"

class UserFaculty(models.Model):
    faculty_name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.faculty_name
    
class UserDept(models.Model):
    dept_name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    unique_key = models.ForeignKey(UserFaculty, on_delete=models.CASCADE, related_name="department", null=True, blank=True)
    
    def __str__(self):
        return self.dept_name
    
class UserCourses(models.Model):
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10)
    unique_key = models.ForeignKey(UserFaculty, on_delete=models.CASCADE, related_name="courses", null=True, blank=True)
    
    def __str__(self):
        return f"{self.course_name} ({self.course_code})"
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    faculty = models.ForeignKey(UserFaculty, on_delete=models.CASCADE, related_name="student_faculty", null=True, blank=True)
    department = models.ForeignKey(UserDept, on_delete=models.CASCADE, related_name="student_department", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student} \n{self.faculty} \n{self.department}"
    
class Lecturer(models.Model):
    name = models.CharField(max_length=255)
    student = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.name
    
class CourseEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="students", null=True, blank=True)
    course = models.ForeignKey(UserCourses, on_delete=models.CASCADE, related_name="courses", null=True, blank=True)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student}, {self.course}"