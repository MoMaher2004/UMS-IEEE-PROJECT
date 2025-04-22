import import_samples

fee = import_samples.university_sample()

user = None

def mip(s=''):
    '''
    this function is a modified version of input() to accept 'EXIT' clause to exit from the program
    '''
    i = input(s)
    if i == 'EXIT':
        exit()
    return i

def student_auth():
    '''
    this function will be called if the user is a student
    '''
    print('choose any option you want from the following list by entering the number of option:')
    print('''
        1) update password
        2) view your data
        3) generate GPA report
        4) view course schedule
        5) get enrolled in a course
    ''')
    option = mip('choose an option:\n')
    while int(option) not in range(1, 5):
        option = mip('enter a valid option:\n')
    
    if option == '1':
        user.password = mip('enter a password\n')
    elif option == '2':
        print(user)
    elif option == '3':
        fee.generate_gpa_report(user)
    elif option == '4':
        fee.course_schedule(fee.search_course(mip('enter course code')))
    elif option == '5':
        course = fee.search_course(mip('enter course code\n'))
        if course:
            fee.enroll_students_in_courses(course, user)

def professor_auth():
    '''
    this function will be called if the user is a professor
    '''
    print('choose any option you want from the following list by entering the number of option:')
    print('''
        1) update password
        2) view your data
        3) view course schedule
        4) view students in a course
    ''')
    option = mip('choose an option:\n')
    while int(option) not in range(1, 4):
        option = mip('enter a valid option:\n')
    
    if option == '1':
        user.password = mip('enter a password\n')
    elif option == '2':
        print(user)
    elif option == '3':
        fee.course_schedule(fee.search_course(mip('enter course code')))
    elif option == '4':
        print(*fee.search_course(mip('enter course code')).enrolled_students)

def hr_auth():
    '''
    this function will be called if the user is a hr
    '''
    print('choose any option you want from the following list by entering the number of option:')
    print('''
        1) update password
        2) view your data
        3) add student
        4) view students
        5) delete student
        6) add professor
        7) view professors
        8) delete professor
        9) update student grade
        10) generate gpa report
        11) view course schedule
    ''')
    option = mip('choose an option:\n')
    while int(option) not in range(1, 11):
        option = mip('enter a valid option:\n')
    
    if option == '1':
        user.password = mip('enter a password\n')
    elif option == '2':
        print(user)
    elif option == '3':
        new_student = fee.Student(
            student_id=mip('enter student id\n'),
            name=mip('enter student name\n'),
            age=mip('enter student age\n'),
            gender=mip('enter student gender\n'),
            password=mip('enter student temporary password\n'),
        )
        fee.add_student(new_student)
        print('new student was added successfully\n', new_student)
    elif option == '4':
        fee.view_students()
    elif option == '5':
        fee.delete_student(mip('enter student id\n'))
    elif option == '6':
        new_professor = fee.Professor(
            professor_id=mip('enter professor id\n'),
            name=mip('enter professor name\n'),
            age=mip('enter professor age\n'),
            gender=mip('enter professor gender\n'),
            password=mip('enter professor temporary password\n'),
            department=mip('enter professor department\n')
        )
        fee.add_professor(new_professor)
        print('new professor was added successfully\n', new_professor)
    elif option == '7':
        fee.view_professors()
    elif option == '8':
        fee.delete_professor(mip('enter professor id\n'))
    elif option == '9':
        fee.update_student_grade(fee.search_student(mip('enter student id\n')), mip('enter grade\n'))
    elif option == '10':
        fee.generate_gpa_report(fee.search_student(mip('enter student id\n')))
    elif option == '11':
        fee.course_schedule(fee.search_course(mip('enter course code')))

def principle_auth():
    '''
    this function will be called if the user is a principle
    '''
    print('choose any option you want from the following list by entering the number of option:')
    print('''
        1) update password
        2) view your data
        3) add student
        4) view students
        5) delete student
        6) add professor
        7) view professors
        8) delete professor
        9) add admin
        10) view admins
        11) delete admin
        12) assign professor to department
        13) create course
        14) assign course to professor
        15) update student grade
        16) generate gpa report
        17) view course schedule
    ''')
    option = mip('choose an option:\n')
    while int(option) not in range(1, 17):
        option = mip('enter a valid option:\n')
    
    if option == '1':
        user.password = mip('enter a password\n')
    elif option == '2':
        print(user)
    elif option == '3':
        new_student = fee.Student(
            student_id=mip('enter student id\n'),
            name=mip('enter student name\n'),
            age=mip('enter student age\n'),
            gender=mip('enter student gender\n'),
            password=mip('enter student temporary password\n'),
        )
        fee.add_student(new_student)
        print('new student was added successfully\n', new_student)
    elif option == '4':
        fee.view_students()
    elif option == '5':
        fee.delete_student(mip('enter student id\n'))
    elif option == '6':
        new_professor = fee.Professor(
            professor_id=mip('enter professor id\n'),
            name=mip('enter professor name\n'),
            age=mip('enter professor age\n'),
            gender=mip('enter professor gender\n'),
            password=mip('enter professor temporary password\n'),
            department=mip('enter professor department\n')
        )
        fee.add_professor(new_professor)
        print('new professor was added successfully\n', new_professor)
    elif option == '7':
        fee.view_professors()
    elif option == '8':
        fee.delete_professor(mip('enter professor id\n'))
    elif option == '9':
        new_admin = fee.Admin(
            admin_id=mip('enter admin id\n'),
            name=mip('enter admin name\n'),
            age=mip('enter admin age\n'),
            gender=mip('enter admin gender\n'),
            password=mip('enter admin temporary password\n'),
            access_level='hr'
        )
        fee.add_admin(new_admin)
        print('new admin was added successfully\n', new_admin)
    elif option == '10':
        fee.view_admins()
    elif option == '11':
        fee.delete_admin(mip('enter admin id\n'))
    elif option == '12':
        fee.assign_professor_to_department(fee.search_professor(mip('enter professor id\n')), fee.search_department(mip('enter department name\n')))
    elif option == '13':
        new_course = fee.Course(
            course_code=mip('enter course code\n'),
            course_name=mip('enter course name\n')
        )
        fee.create_course(new_course)
        print('new course was added successfully')
    elif option == '14':
        fee.assign_course_to_professor(fee.search_course(mip('enter course code')) ,fee.search_professor(mip('enter professor id\n')))
    elif option == '15':
        fee.update_student_grade(fee.search_student(mip('enter student id\n')), mip('enter grade\n'))
    elif option == '16':
        fee.generate_gpa_report(fee.search_student(mip('enter student id\n')))
    elif option == '17':
        fee.course_schedule(fee.search_course(mip('enter course code')))


print('hi !')
print('GENERAL NOTE:\nat anytime you enter \'EXIT\' the program will exit')

id = int(mip('please enter your id:\n'))
pw = str(mip('please enter your password:\n'))
user = fee.login(id, pw)
if user is None:
    print('enter correct data')
    exit()

auth = user['auth']
user = user['user']
print('hello', user.name)

while True:
    if auth == 'student':
        student_auth()
    elif auth == 'professor':
        professor_auth()
    elif auth == 'admin' and user.access_level == 'hr':
        hr_auth()
    elif auth == 'admin' and user.access_level == 'principle':
        principle_auth()