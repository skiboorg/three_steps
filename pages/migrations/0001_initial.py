# Generated by Django 2.2.7 on 2020-06-29 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Название вакансии')),
                ('option1', models.CharField(blank=True, default='Бесплатное обучение', max_length=255, null=True, verbose_name='Опция вакансии')),
                ('option2', models.CharField(blank=True, default='Быстрый старт в профессии под руководством опытного наставника', max_length=255, null=True, verbose_name='Опция вакансии')),
                ('option3', models.CharField(blank=True, default='Перспективы профессионального развития и карьерного роста', max_length=255, null=True, verbose_name='Опция вакансии')),
                ('option4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Опция вакансии')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна ?')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='VacancyApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Имя')),
                ('email', models.CharField(max_length=255, null=True, verbose_name='Email')),
                ('resume', models.FileField(blank=True, null=True, upload_to='', verbose_name='Резюме')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('vacancy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Vacancy', verbose_name='Вакаксия')),
            ],
            options={
                'verbose_name': 'Отзыв на вакансию',
                'verbose_name_plural': 'Отзывы на вакансии',
            },
        ),
    ]
