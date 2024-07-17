from django.contrib import admin

# Register your models here.
from .models import ClassPeriod


# class ClassPeriodAdmin(admin.ModelAdmin):
#     list_display = ('class_id', 'course', 'start_time', 'end_time','classroom_period','day_of_week','teachers_period')

admin.site.register(ClassPeriod)