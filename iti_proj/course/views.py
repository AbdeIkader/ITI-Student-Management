from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseCreateForm

def course_list(request):
    return render(request, 'course/course_list.html', {'courses': Course.objects.all()})

def course_create(request):
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Course.objects.create(code=data['code'], name=data['name'])
            return redirect('course_list')
    else:
        form = CourseCreateForm()
    return render(request, 'course/course_form.html', {'form': form, 'title': 'Create Course'})

def course_delete(request, code):
    course = get_object_or_404(Course, pk=code)
    course.delete()
    return redirect('course_list')
