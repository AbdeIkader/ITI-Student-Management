from django import forms
from .models import Student
from course.models import Course

class StudentForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model  = Student
        fields = ['name', 'age', 'image', 'date_of_birth', 'courses']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age < 18:
            raise forms.ValidationError('Age must be at least 18')
        return age
