class Person:
    def __init__(self, name, age, gender, ID, password):
        self._ID = ID
        self._name = name
        self._gender = gender
        self._age = age
        self._password = password

    @property
    def ID(self):
        return self._ID
    
    @ID.setter
    def ID(self, val):
        if all(10e5 < val < 10e6 and val % 1 == 0):
            self._ID = val
        else:
            raise ValueError('ID must be an int between 100000 and 1000000')

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = val

    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, val):
        if str.lower(val) in ('male', 'female'):
            self._gender = val
        else:
            raise ValueError('only male and female are recogonized')

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, val):
        if val > 18:
            self._age = val
        else:
            raise ValueError('you are to small to be in the university')

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, val):
        if len(val) > 7:
            self._password = val
        else:
            raise ValueError('password must be at least 8 chars')

class Student(Person):
    def __init__(self, name, age, gender, student_id, password, enrolled_courses=[], GPA=None):
        super().__init__(name, age, gender, student_id, password)
        self._enrolled_courses = enrolled_courses
        self._GPA = GPA

    def __str__(self):
        return f"ID: {self._ID}\nname: {self._name}\nage: {self._age}\ngender: {self._gender}\nGPA: {self._GPA}\nenrolled courses: {self._enrolled_courses}\n"

    @property
    def enrolled_courses(self):
        return self._enrolled_courses
    
    @enrolled_courses.setter
    def enrolled_courses(self, val):
        self._enrolled_courses = val

    @property
    def GPA(self):
        return self._GPA
    
    @GPA.setter
    def GPA(self, val):
        if val >= 0:
            self._GPA = val
        else:
            raise ValueError('negative GPA ! Are you that stupid ?')

class Professor(Person):
    def __init__(self, name, age, gender, professor_id, password, department=None, courses_taught=[]):
        super().__init__(name, age, gender, professor_id, password)
        self._department = department
        self._courses_taught = courses_taught

    def __str__(self):
        return f"ID: {self._ID}\nname: {self._name}\nage: {self._age}\ngender: {self._gender}\ndepartment: {self._department}\ncourses taught: {self._courses_taught}\n"

    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, val):
        self._department = val

    @property
    def courses_taught(self):
        return self._courses_taught
    
    @courses_taught.setter
    def courses_taught(self, val):
        self._courses_taught = val

class Admin(Person):
    def __init__(self, name, age, gender, admin_id, password, access_level='hr'):
        super().__init__(name, age, gender, admin_id, password)
        self._access_level = access_level

    def __str__(self):
        return f"ID: {self._ID}\nname: {self._name}\nage: {self._age}\ngender: {self._gender}\naccess level: {self._access_level}\n"

    @property
    def access_level(self):
        return self._access_level
    
    @access_level.setter
    def access_level(self, val):
        if str.lower(val) in ['hr', 'principle']:
            self._access_level = val
        else:
            raise ValueError('who are you ?')

class Department:
    def __init__(self, name, head_of_department, affiliates=[]):
        self._name = name
        self._head_of_department = head_of_department
        self._affiliates = affiliates

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = val

    @property
    def head_of_department(self):
        return self._head_of_department
    
    @head_of_department.setter
    def head_of_department(self, val):
        self._head_of_department = val

    @property
    def affiliates(self):
        return self._affiliates
    
    @affiliates.setter
    def affiliates(self, val):
        self._affiliates = val

class Course:
    def __init__(self, course_code, course_name, assigned_professor=None, enrolled_students=[]):
        self._course_code = course_code
        self._course_name = course_name
        self._assigned_professor = assigned_professor
        self._enrolled_students = enrolled_students

    @property
    def course_code(self):
        return self._course_code
    
    @course_code.setter
    def course_code(self, val):
        self._course_code = val

    @property
    def course_name(self):
        return self._course_name
    
    @course_name.setter
    def course_name(self, val):
        self._course_name = val

    @property
    def assigned_professor(self):
        return self._assigned_professor
    
    @assigned_professor.setter
    def assigned_professor(self, val):
        self._assigned_professor = val

    @property
    def enrolled_students(self):
        return self._enrolled_students
    
    @enrolled_students.setter
    def enrolled_students(self, val):
        self._enrolled_students = val

class Schedule:
    def __init__(self, room_number, course_assigned, time_slots=[]):
        self._time_slots = time_slots
        self._room_number = room_number
        self._course_assigned = course_assigned

    @property
    def time_slots(self):
        return self._time_slots
    
    @time_slots.setter
    def time_slots(self, val):
        self._time_slots = val

    @property
    def room_number(self):
        return self._room_number
    
    @room_number.setter
    def room_number(self, val):
        self._room_number = val

    @property
    def course_assigned(self):
        return self._course_assigned
    
    @course_assigned.setter
    def course_assigned(self, val):
        self._course_assigned = val

class University:
    def __init__(self, departments=[], students=[], professors=[], admins=[], courses=[] ,schedules=[]):
        self._departments = departments
        self._students = students
        self._professors = professors
        self._admins = admins
        self._courses = courses
        self._schedules = schedules

    @property
    def departments(self):
        return self._departments
    
    @departments.setter
    def departments(self, val):
        self._departments = val

    @property
    def students(self):
        return self._students
    
    @students.setter
    def students(self, val):
        self._students = val

    @property
    def professors(self):
        return self._professors
    
    @professors.setter
    def professors(self, val):
        self._professors = val

    @property
    def admins(self):
        return self._admins
    
    @admins.setter
    def admins(self, val):
        self._admins = val

    @property
    def courses(self):
        return self._courses
    
    @courses.setter
    def courses(self, val):
        self._courses = val

    @property
    def schedules(self):
        return self._schedules
    
    @schedules.setter
    def schedules(self, val):
        self._schedules = val

    # Manage students

    def add_student(self, student):
        self._students.append(student)

    def view_students(self):
        for student in self._students:
            print(student, '----------------------')

    def delete_student(self, id):
        for student in self._students:
            if student.ID == id:
                print(f'student {student.name} deleted')
                del student
                return
        print('student not found')

    # Manage professors

    def add_professor(self, professor):
        self._professors.append(professor)

    def view_professors(self):
        for professor in self._professors:
            print(professor, '----------------------')

    def delete_professor(self, id):
        for professor in self._professors:
            if professor.ID == id:
                print(f'professor {professor.name} deleted')
                del professor
                return
        print('professor not found')

    # Manage admins

    def add_admin(self, admin):
        self._admins.append(admin)

    def view_admins(self):
        for admin in self._admins:
            print(admin, '----------------------')

    def delete_admin(self, id):
        for admin in self._admins:
            if admin.ID == id:
                print(f'admin {admin.name} deleted')
                del admin
                return
        print('admin not found')

    # assign professor to department

    def assign_professor_to_department(professor, department):
        department.affiliates = department.affiliates + professor
        professor.department = department

    # Create and assign courses to departments and professors

    def create_course(self, course):
        self._courses.append(course)

    def assign_course_to_professor(course, professor):
        professor.courses_taught = course + professor.courses_taught

    # Enroll students in courses

    def enroll_students_in_courses(course, student):
        student.enrolled_courses = course + student.enrolled_courses
        course.enrolled_students = student + course.enrolled_students

    # Assign and update student grades

    def update_student_grade(student, GPA):
        student.GPA = GPA

    # Generate GPA reports

    def generate_gpa_report(student):
        pass

    # View course schedule

    def course_schedule(self, course):
        courseCode = course.course_code
        for schedule in self._schedules:
            if schedule.course_assigned.course_code == courseCode:
                print(f'room:{schedule.room_number}\ntime slots:', *schedule.room_number)


    # login

    def login(self, ID, password):
        if ID == '' or password == '':
            raise AttributeError('enter all required data')
        
        for student in self._students:
            if student.ID == ID:
                if student.password == password:
                    return {'auth': 'student', 'user': student}
                else:
                    raise AttributeError('user was not found')
        
        for professor in self._professors:
            if professor.ID == ID:
                if professor.password == password:
                    return {'auth': 'professor', 'user': professor}
                else:
                    raise AttributeError('user was not found')
        
        for admin in self._admins:
            if admin.ID == ID:
                if admin.password == password:
                    return {'auth': 'admin', 'user': admin}
                else:
                    raise AttributeError('user was not found')
                
    # search for a course

    def search_course(self, code):
        for course in self._courses:
            if course.course_code == code:
                return course
        return False
                
    # search for a department

    def search_department(self, name):
        for department in self._departments:
            if department.name == name:
                return department
        return False
                
    # search for a student

    def search_student(self, id):
        for student in self._students:
            if student.id == id:
                return student
        return False
                
    # search for a professor

    def search_professor(self, id):
        for professor in self._professors:
            if professor.id == id:
                return professor
        return False
                
    # search for a admin

    def search_admin(self, id):
        for admin in self._admins:
            if admin.id == id:
                return admin
        return False
