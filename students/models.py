from django.db import models

class Student(models.Model):
    CLASS_CHOICES = [
        (1, "Class 1"), (2, "Class 2"), (3, "Class 3"),
        (4, "Class 4"), (5, "Class 5"), (6, "Class 6"),
        (7, "Class 7"), (8, "Class 8"), (9, "Class 9"),
        (10, "Class 10"), (11, "Class 11"), (12, "Class 12"),
    ]

    name = models.CharField(max_length=100)
    student_class = models.IntegerField(choices=CLASS_CHOICES)
    batch = models.CharField(max_length=50)
    parent_mobile = models.CharField(max_length=15)
    join_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (Class {self.student_class})"
