from django.db import models

# Create your models here.
class Course(models.Model):

    course_name = models.CharField(max_length=200, verbose_name='Имя')
    course_start = models.DateTimeField(auto_now=True)
    course_end = models.DateTimeField(auto_now=True)
    lecture_quant = models.CharField(max_length=200, verbose_name='Лекция')

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
