# Generated by Django 5.0.7 on 2024-07-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_course_students'),
        ('student', '0003_alter_students_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students_course',
            field=models.ManyToManyField(to='student.students'),
        ),
    ]
