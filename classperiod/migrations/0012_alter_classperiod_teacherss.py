# Generated by Django 5.0.7 on 2024-07-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0011_remove_classperiod_classroom_period_and_more'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classperiod',
            name='teacherss',
            field=models.ManyToManyField(to='teachers.teacher'),
        ),
    ]
