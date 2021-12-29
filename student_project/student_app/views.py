from django.shortcuts import render
from student_app.models import Student
from student_app import forms


# Create your views here.

def home(request):
    return render(request, 'second_app/home.html', context={'home': "I am from Home Page"})


def student(request):
    stu_list = Student.objects.order_by('stu_name')
    stu_dict = {'student': stu_list}
    return render(request, 'second_app/student.html', context=stu_dict)


def student_view(request):
    form = forms.StudentForm()

    if request.method == 'POST':
        form = forms.StudentForm(request.POST)

        if form.is_valid():
            print("Validation Success")
            print(f"Name is {form.cleaned_data['name']}")
            print(f"Age is {form.cleaned_data['age']}")
            print(f"Email is {form.cleaned_data['email']}")
    return render(request, 'second_app/studentform.html', {"form": form})
