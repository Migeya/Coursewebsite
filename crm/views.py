from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from django.views.generic import DetailView

# Create your views here.
# Отображение главной страницы
def first_page(request):
    object_list = Course.objects.all()
    form = CourseForm()
    return render(request, 'crm/index.html', {'object_list': object_list,
                                            'form': form})

# Отображение полной инормации о курсе
class CourseDetailView(DetailView):
    model = Course
    template_name = 'crm/details_view.html'
    context_object_name = 'course'


def thanks_page(request):
    pass
    # name = request.GET['name']
    # start = request.GET['start']
    # end = request.GET['end']
    # quantity = request.GET['quantity']
    # element = Course(course_name=name, course_start=start, course_end=end, lecture_quant=quantity)
    # element.save()
    # return render(request, 'crm/thanks_page.html', {'name': name,
    #                                              'start': start,
    #                                              'end': end,
     #                                             'quantity': quantity})

# Страница создания нового курса
def create(request):
    error = ''
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неправильно заполненая форма'

    form = CourseForm()
    data ={
        'form': form,
        'error': error
    }

    return render(request, 'crm/create.html', data)