# Generated by Django 4.1.4 on 2023-03-04 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0011_animaltype_shelter_animal_types_and_more'),
        ('info', '0007_alter_helparticle_text_alter_news_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(help_text='Введите название должности', max_length=30, verbose_name='Доложность')),
                ('description', models.TextField(help_text='Опишите подробности вакансии', max_length=500, verbose_name='Описание')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('is_closed', models.BooleanField(default=False, verbose_name='Вакансия закрыта')),
                ('shelter', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='vacancy', to='shelters.shelter', verbose_name='Вакансия в приют')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.DeleteModel(
            name='OwnVacancy',
        ),
        migrations.DeleteModel(
            name='ShelterVacancy',
        ),
    ]
