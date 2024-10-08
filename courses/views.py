from django.shortcuts import render
from .models import Group, User


def groups_page(request):

    if request.method == "POST":
        course_title = request.POST["kurs_mavzusi"]
        course_category = request.POST["kurs_nomi"]
        description = request.POST["qisqa_malumot"]
        course_price = request.POST["kurs_narxi"]
        course_duration = request.POST["kurs_davomiyligi"]
        rating = request.POST["reyting"]
        learning_style = request.POST["oqish_uslubi"]
        phone_number = request.POST["murojaat_uchun"]
        course_level = request.POST["kurs_darajasi"]

        print(
            course_title,
            course_category,
            description,
            course_price,
            course_duration,
            rating,
            learning_style,
            phone_number,
            course_level,
        )

        new_groups = Group.objects.create(
            course_title=course_title,
            course_category=course_category,
            description=description,
            course_price=course_price,
            course_duration=course_duration,
            rating=rating,
            learning_style=learning_style,
            phone_number=phone_number,
            course_level=course_level,
        )

    groups = Group.objects.all()

    context = {"groups": groups}

    return render(request, "group.html", context)


def users_page(request):

    if request.method == "POST":
        name = request.POST["ismi"]
        surname = request.POST["familiyasi"]
        age = request.POST["yoshi"]
        phone = request.POST["telefon_raqami"]
        email = request.POST["email_pochtasi"]
        interests = request.POST["qiziqishlari"]
        grade = request.POST["darajasi"]

        print(name, surname, age, phone, email, interests, grade)

        new_users = User.objects.create(
            name=name,
            surname=surname,
            age=age,
            phone=phone,
            email=email,
            interests=interests,
            grade=grade,
        )

    users = User.objects.all()

    context = {"users": users}

    return render(request, "user.html", context)
