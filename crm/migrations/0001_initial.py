# Generated by Django 3.2.1 on 2021-05-05 16:19

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
                ('course_start', models.DateTimeField(auto_now=True)),
                ('course_end', models.DateTimeField(auto_now=True)),
                ('lecture_quant', models.CharField(max_length=200, verbose_name='Лекция')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
