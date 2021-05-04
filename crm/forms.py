from .models import Course
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_start', 'course_end', 'lecture_quant', 'text_all']

        widgets = {
            'course_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название курса'
            }),
            'course_start': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Начало курса'
            }),
            'course_end': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Конец курса'
            }),
            'lecture_quant': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество лекций'
            }),
            'text_all': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание лекций'
            })
        }