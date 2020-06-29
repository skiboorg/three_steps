# Generated by Django 2.2.7 on 2020-06-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=255, null=True, verbose_name='Город')),
                ('town', models.CharField(blank=True, max_length=255, null=True, verbose_name='Город')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Контактное лицо ')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон ')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('currency_type', models.CharField(max_length=15, verbose_name='Валюта')),
                ('price', models.IntegerField(null=True, verbose_name='Цена')),
                ('street', models.CharField(max_length=255, null=True, verbose_name='Улица')),
                ('street_number', models.CharField(max_length=255, null=True, verbose_name='Номер дома')),
                ('floor', models.IntegerField(blank=True, null=True, verbose_name='Этаж')),
                ('floor_total', models.IntegerField(blank=True, null=True, verbose_name='Этажность')),
                ('rooms', models.CharField(blank=True, max_length=10, null=True, verbose_name='Комнат')),
                ('square_total', models.IntegerField(blank=True, null=True, verbose_name='Площадь общая')),
                ('square_kitchen', models.IntegerField(blank=True, null=True, verbose_name='Площадь кухни')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('is_viewed', models.BooleanField(default=False, verbose_name='Обработана ?')),
            ],
            options={
                'verbose_name': 'Заявка на консультацию',
                'verbose_name_plural': 'Заявки на консультацию',
            },
        ),
    ]
