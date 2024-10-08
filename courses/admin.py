from django.contrib import admin
from .models import Group, User


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "course_title",
        "course_category",
        "description",
        "course_price",
        "course_duration",
        "rating",
        "created_date",
        "updated_date",
        "learning_style",
        "phone_number",
        "course_level",
    ]


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "surname",
        "age",
        "phone",
        "email",
        "interests",
        "grade",
    ]
    list_editable = ["name", "surname", "phone", "email"]


admin.site.register(Group)
admin.site.register(User)
