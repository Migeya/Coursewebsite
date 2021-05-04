# Generated by Django 3.2.1 on 2021-05-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('course_start', models.DateTimeField('Старт')),
                ('course_end', models.DateTimeField('Конец')),
                ('lecture_quant', models.CharField(max_length=200, verbose_name='Лекция')),
                ('text_all', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
