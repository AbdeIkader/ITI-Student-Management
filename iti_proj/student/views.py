from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import Student, StudentCourse
from .forms import StudentForm

def student_list(request):
    students = Student.objects.prefetch_related('courses').all().order_by('name')
    return render(request, 'student/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student/student_detail.html', {'student': student})

@transaction.atomic
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            selected_courses = form.cleaned_data['courses']
            for course in selected_courses:
                StudentCourse.objects.create(student=student, course=course)
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form': form, 'title': 'Create Student'})

@transaction.atomic
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            StudentCourse.objects.filter(student=student).delete()
            selected_courses = form.cleaned_data['courses']
            for course in selected_courses:
                StudentCourse.objects.create(student=student, course=course)
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/student_form.html', {'form': form, 'title': 'Update Student'})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')
