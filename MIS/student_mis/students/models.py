from django.db import models

class Student(models.Model):
    REQ_NO_CHOICES = [(i, i) for i in range(1, 10001)]
    YEAR_CHOICES = [
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third'),
        ('Fourth', 'Fourth'),
    ]

    ReqNo = models.PositiveIntegerField(unique=True, choices=REQ_NO_CHOICES)
    Name = models.CharField(max_length=100)
    Branch = models.CharField(max_length=50)
    Year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    Address = models.TextField()
    State = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Name} ({self.ReqNo})"
