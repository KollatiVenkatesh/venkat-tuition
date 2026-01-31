from django.db import models
from students.models import Student

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)  # Example: "March 2026"
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    payment_date = models.DateField(null=True, blank=True)

    @property
    def status(self):
        return "PAID" if self.paid_amount >= self.total_amount else "PENDING"

    def __str__(self):
        return f"{self.student.name} - {self.month}"
