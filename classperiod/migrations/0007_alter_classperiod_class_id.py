# Generated by Django 5.0.7 on 2024-07-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0006_remove_classperiod_id_classperiod_class_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classperiod',
            name='class_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
