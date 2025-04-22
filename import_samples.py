'''
in this file i will create some samples
students x100
professors x10
admins(hr) x2
admins(principle) x1
departments x3
courses x10
schedule x10

each user will have default password = their id

default student ids varies from 100001 to 100101
default professors ids varies from 20001 to 200011
default hrs ids varies from 300001 to 300002
default principle id is 300003

this file will be made with the help of AI (i won't write a lot of data)
'''

import ums
import random

female_first_names = [
    "Emma", "Olivia", "Ava", "Isabella", "Sophia",
    "Charlotte", "Mia", "Amelia", "Harper", "Evelyn",
    "Abigail", "Emily", "Elizabeth", "Mila", "Ella",
    "Avery", "Sofia", "Camila", "Aria", "Scarlett",
    "Victoria", "Madison", "Luna", "Grace", "Chloe",
    "Penelope", "Layla", "Riley", "Zoey", "Nora",
    "Lily", "Eleanor", "Hannah", "Lillian", "Addison",
    "Aubrey", "Ellie", "Stella", "Natalie", "Zoe",
    "Leah", "Hazel", "Violet", "Aurora", "Savannah",
    "Audrey", "Brooklyn", "Bella", "Claire", "Skylar"
]

female_last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

male_first_names = [
    "Liam", "Noah", "William", "James", "Oliver",
    "Benjamin", "Elijah", "Lucas", "Mason", "Logan",
    "Alexander", "Ethan", "Jacob", "Michael", "Daniel",
    "Henry", "Jackson", "Sebastian", "Aiden", "Matthew",
    "Samuel", "David", "Joseph", "Carter", "Owen",
    "Wyatt", "John", "Jack", "Luke", "Jayden",
    "Dylan", "Grayson", "Levi", "Isaac", "Gabriel",
    "Julian", "Mateo", "Anthony", "Jaxon", "Lincoln",
    "Joshua", "Christopher", "Andrew", "Theodore", "Caleb",
    "Ryan", "Asher", "Nathan", "Thomas", "Leo",
    "Isaiah", "Charles", "Josiah", "Hudson", "Christian",
    "Hunter", "Connor", "Eli", "Ezra", "Aaron"
]

male_last_names = [
    "Perez", "Thompson", "White", "Harris", "Sanchez",
    "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott",
    "Torres", "Nguyen", "Hill", "Flores", "Green",
    "Adams", "Nelson", "Baker", "Hall", "Rivera",
    "Campbell", "Mitchell", "Carter", "Roberts", "Gomez",
    "Phillips", "Evans", "Turner", "Diaz", "Parker",
    "Cruz", "Edwards", "Collins", "Reyes", "Stewart",
    "Morris", "Morales", "Murphy", "Cook", "Rogers"
]

students = []
professors = []
admins = [
    ums.Admin(
        admin_id=300001,
        name=random.choice(female_first_names) + ' ' + random.choice(female_last_names),
        age=random.randint(40, 80),
        gender='female',
        password=str(300001)
    ),
    ums.Admin(
        admin_id=300002,
        name=random.choice(male_first_names) + ' ' + random.choice(male_last_names),
        age=random.randint(40, 80),
        gender='male',
        password=str(300002)
    ),
    ums.Admin(
        admin_id=300003,
        name=random.choice(male_first_names) + ' ' + random.choice(male_last_names),
        age=random.randint(40, 80),
        gender='male',
        password=str(300003),
        access_level='principle'
    )
]


tmp = [
    ums.Student(
        student_id=i,
        name=random.choice(female_first_names) + ' ' + random.choice(female_last_names),
        age=random.randint(18, 22),
        gender='female',
        password=str(i)
    )
    for i in range(100001, 100051)
]

students.extend(tmp)

tmp = [
    ums.Student(
        student_id=i,
        name=random.choice(male_first_names) + ' ' + random.choice(male_last_names),
        age=random.randint(18, 22),
        gender='male',
        password=str(i)
    )
    for i in range(100051, 100101)
]

students.extend(tmp)

tmp = [
    ums.Professor(
        professor_id=i,
        name=random.choice(male_first_names) + ' ' + random.choice(male_last_names),
        age=random.randint(30, 80),
        gender='male',
        password=str(i)
    )
    for i in range(200001, 200006)
]

professors.extend(tmp)

tmp = [
    ums.Professor(
        professor_id=i,
        name=random.choice(female_first_names) + ' ' + random.choice(female_last_names),
        age=random.randint(30, 80),
        gender='female',
        password=str(i)
    )
    for i in range(200006, 200011)
]

professors.extend(tmp)

departments = [
    ums.Department(
        name='computer science',
        head_of_department=random.choice(professors)
    ),
    ums.Department(
        name='control and automation',
        head_of_department=random.choice(professors)
    ),
    ums.Department(
        name='communication',
        head_of_department=random.choice(professors)
    )
]

courseSamples = {
    "CS101": "Introduction to Programming",
    "CS205": "Data Structures and Algorithms",
    "CS310": "Database Systems",
    "CS415": "Artificial Intelligence",
    "CA201": "Control Systems Engineering",
    "CA305": "Robotics and Automation",
    "CA410": "Industrial Control Systems",
    "ELEC102": "Digital Electronics",
    "ELEC220": "Microprocessors & Embedded Systems",
    "ELEC350": "Signal Processing",
}

courses = [ums.Course(
    course_code=key,
    course_name=val
)
for key, val in courseSamples.items()
]

schedules = [
    ums.Schedule(
        room_number=random.randint(1, 10),
        course_assigned=course
    )
    for course in courses
]

def university_sample():
    return ums.University(
        departments=departments,
        admins=admins,
        courses=courses,
        professors=professors,
        schedules=schedules,
        students=students
    )