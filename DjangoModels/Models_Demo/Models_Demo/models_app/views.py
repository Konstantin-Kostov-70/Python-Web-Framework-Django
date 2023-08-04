from django.shortcuts import render, redirect, get_object_or_404

from Models_Demo.models_app.models import Student, University


def index(request):
    all_students = Student.objects.all()
    filtered_students = Student.objects.filter(university_id=2)
    all_universities = University.objects.all()
    get_university = University.objects.get(id=2)
    context = {
        'all_students': all_students,
        'filtered_students': filtered_students,
        'all_universities': all_universities,
        'get_university': get_university,
    }

    return render(request, 'index.html', context)


def delete_students(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('home')


def students_details(request, pk):
    student = Student.objects.get(pk=pk)
    university_id = student.university_id
    university = University.objects.get(pk=university_id)
    context = {
        'student': student,
        'university': university
    }
    return render(request, 'details.html', context)


def university_details(request, pk, slug):
    context = {
        'university': University.objects.get(pk=pk, slug=slug)
    }
    return render(request, 'university_details.html', context)
