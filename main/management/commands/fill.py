from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Petrov', 'first_name': 'Peter'},
            {'last_name': 'Ivanov', 'first_name': 'Ivan'},
            {'last_name': 'Semenov', 'first_name': 'Semen'},
            {'last_name': 'Kazantsev', 'first_name': 'Yuriy'}
        ]

        #for student_item in student_list:
        #    Student.objects.create(**student_item)

        students_for_create = []
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )

        Student.objects.bulk_create(students_for_create)




