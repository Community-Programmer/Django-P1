from django.db import models

class Performance(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_date = models.DateField()