from django.urls import path;
from .views import StudentListView, ClassPeriodListView

urlpatterns= [
    path("students/",StudentListView.as_view(), name="student_List_View"),
]
urlpatterns = [
    path("periods/",ClassPeriodListView.as_view(), name="classperiod_list_view"),
]