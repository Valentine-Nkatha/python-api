# Generated by Django 5.1 on 2024-08-15 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('course', '0006_remove_course_students'),
        ('teachers', '0002_alter_teacher_teachers_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teachers_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teachers_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
    ]
