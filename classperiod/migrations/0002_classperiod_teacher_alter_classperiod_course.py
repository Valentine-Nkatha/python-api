# Generated by Django 5.0.7 on 2024-07-17 13:16

import django.db.models.deletion
from django.db import migrations, models

# def set_default_teacher(apps, schema_editor):
#     Teacher = apps.get_model('teacher', 'Teacher')
#     default_teacher = Teacher.objects.first()  # Set the appropriate default teacher
#     ClassPeriod = apps.get_model('classperiod', 'ClassPeriod')
#     ClassPeriod.objects.filter(teacher_id=None).update(teacher=default_teacher)


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0001_initial'),
        ('course', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classperiod',
            name='teacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
        ),
        # migrations.AlterField(
        #     model_name='classperiod',
        #     name='course',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        # ),
    ]
