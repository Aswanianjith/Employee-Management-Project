from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Master(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True, verbose_name="Active")
    created_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ['-isactive']

class Transaction(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Name(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Names"

    def __str__(self):
        return self.name

class Designation(models.Model):
    designation = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Designations"

    def __str__(self):
        return self.designation

class Salary(models.Model):
    salary = models.IntegerField()

    class Meta:
        verbose_name_plural = "Salaries"

    def __str__(self):
        return str(self.salary)



# Existing models...

class Employee(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.designation}"

# Make sure to import Employee in admin.py
