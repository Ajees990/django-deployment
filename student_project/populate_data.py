import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_project.settings')

import django

django.setup()

import random
from student_app.models import Student
from faker import Faker

fakegen = Faker()

subjects = ['Tamil', 'English']


def populate(N=10):
    for entry in range(N):
        fake_name = fakegen.name()
        fake_age = random.randint(1, 30)
        fake_subject = random.choice(subjects)
        fake_country = fakegen.city()

        student = Student.objects.get_or_create(stu_name=fake_name, stu_age=fake_age,
                                                stu_subject=fake_subject, stu_country=fake_country)


if __name__ == '__main__':
    print("populating script")
    populate(N=10)
    print("populating completed")
