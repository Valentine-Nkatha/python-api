# Generated by Django 5.0.7 on 2024-07-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_rename_teachers_id_teacher_teachers_national_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teaachers_hobby',
            field=models.CharField(default='teaching', max_length=20),
        ),
    ]
