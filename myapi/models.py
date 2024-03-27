from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(blank=True, null=True)
    class_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    SEX_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    image = models.ImageField(blank=True, null=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(blank=True, null=True)
    teacher = models.ManyToManyField(Teacher)
    students = models.ManyToManyField(Student)
