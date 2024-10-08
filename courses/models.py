from django.db import models


class Group(models.Model):
    course_title = models.CharField(max_length=150)
    course_category = models.CharField(max_length=150)
    description = models.TextField()
    course_price = models.CharField(max_length=150)
    course_duration = models.CharField(max_length=150)
    rating = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    learning_style = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    course_level = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.course_title} - {self.description}"


class User(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    age = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    interests = models.CharField(max_length=150)
    grade = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.name} - {self.age}"
