from django.shortcuts import render
from .models import Course
from .forms import CourseForm

# Create your views here.
def first_page(request):
    object_list = Course.objects.all()
    form = CourseForm()
    return render(request, './index.html', {'object_list': object_list,
                                            'form': form})

def thanks_page(request):
    name = request.GET['name']
    start = request.GET['start']
    end = request.GET['end']
    quantity = request.GET['quantity']
    element = Course(course_name=name, course_start=start, course_end=end, lecture_quant=quantity)
    element.save()
    return render(request, './thanks_page.html', {'name': name,
                                                  'start': start,
                                                  'end': end,
                                                  'quantity': quantity})