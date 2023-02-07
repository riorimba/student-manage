from django.shortcuts import render, redirect
# from django import forms
from .models import student
# from .forms import studentForm


# Create your views here.
def home(request):
    std = student.objects.all()

    return render(request, "student/home.html", {'std':std})

def add_student(request):
    if request.method == 'POST':
    #     form = studentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("/")
    # else:
    #     form = studentForm()
    # return render(request, "student/add_student.html", {'form': form})
        # form = student(request.POST)
        # if form.is_valid():
        #     student = form.save()
        #     return redirect("student/home.html")
        # print("added")
        #get user input
        students_nim = request.POST.get("student_nim")
        students_name = request.POST.get("student_name")
        students_email = request.POST.get("student_email")
        students_address = request.POST.get("student_address")
        students_phone = request.POST.get("student_phone")

        s = student()
        s.nim = students_nim
        s.name = students_name
        s.email = students_email
        s.address = students_address
        s.phone = students_phone
        s.save()
        return redirect("/")
        
    return render(request, "student/add_student.html", {})

def delete_student(request, id):
    s = student.objects.get(pk=id)
    s.delete()

    return redirect("/")

def edit_student(request, id):
    std = student.objects.get(pk=id)
    return render(request, "student/edit_student.html", {'std':std})

def update_student(request, id):
    if request.method == 'POST':
        std_nim = request.POST.get("student_nim")
        std_name = request.POST.get("student_name")
        std_email = request.POST.get("student_email")
        std_address = request.POST.get("student_address")
        std_phone = request.POST.get("student_phone")

        std = student.objects.get(pk=id)

        std.nim = std_nim
        std.name = std_name
        std.email = std_email
        std.address = std_address
        std.phone = std_phone
        std.save()

        return redirect("/")
    else:
        return render(request, "student/edit_student.html", {'std':std})
