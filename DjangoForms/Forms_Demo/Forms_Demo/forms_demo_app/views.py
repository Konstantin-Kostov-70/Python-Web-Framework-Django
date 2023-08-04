from django.shortcuts import render

from Forms_Demo.forms_demo_app.forms import PersonForm, StudentForm
from Forms_Demo.forms_demo_app.models import Student, University


def index(request):
    name = None
    age = None
    level = None
    if request.method == "GET":
        form = PersonForm()
    else:
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            level = form.cleaned_data['dev_level']

    context = {
        'form': form,
        'name': name,
        'age': age,
        'level': level

    }
    return render(request, 'home.html', context)


def model_forms_view(request):
    universities = None
    name = None
    age = None
    if request.method == 'GET':
        form = StudentForm()
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            universities_query_set = form.cleaned_data.pop('university')
            universities = ", ".join([x.name for x in universities_query_set])
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            form.save()

            # form.save() make the same as code bellow
            # student = Student.objects.create(
            #     **form.cleaned_data
            # )
            # student.university.set(universities_query_set)
            # student.save()

    context = {
        'form': form,
        'universities': universities,
        'name': name,
        'age': age,
    }
    return render(request, 'model-forms.html', context)


def relationship_demo(request):
    student = Student.objects.get(pk=2)
    university = University.objects.get(pk=1)

    # student.university.all() "student have university field" <QuerySet [<University: SoftUni>]>
    # university.student_set.all() "university have not student field and use student_set"
    # <QuerySet [<Student: Konstantin Kostov>, <Student: Stamat>, <Student: Ficus>]>

    related_student = university.student_set.get(pk=2)
    related_university = student.university.get(pk=1)
    context = {
        'student': student,
        'university': university,
        'related_student': related_student,
        'related_university': related_university
    }
    return render(request, 'relationship-demo.html', context)


def create_person_view(request):
    return render(request, 'person.html')
