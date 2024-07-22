from django.urls import path;
from.views import StudentListView, ClassPeriodListView, CourseListView, TeacherListView, ClassListView, StudentDetailView, ClassDetailView, ClassPeriodDetailView, TeacherDetailView, CourseDetailView

urlpatterns= [
    path("students/",StudentListView.as_view(), name="student_list_view"),
     path("classperiods/",ClassPeriodListView.as_view(), name="classperiod_list_view"),
      path("courses/",CourseListView.as_view(), name="course_list_view"),
      path("teachers/",TeacherListView.as_view(), name="teacher_list_view"),
      path("classes/",ClassListView.as_view(),name="class_list_view"),
      path("students/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"),
      path("classes/<int:id>/", ClassDetailView.as_view(), name="class_detail_view"),
      path("classperiods/<int:id>/", ClassPeriodDetailView.as_view(), name="class_detail_view"),
       path("teachers/<int:id>/", TeacherDetailView.as_view(), name="class_detail_view"),
        path("course/<int:id>/", CourseDetailView.as_view(), name="class_detail_view"),
]
# urlpatterns = [
#     path("classperiods/",ClassPeriodListView.as_view(), name="classperiods_list_view"),
# ]
# urlpatterns = [
#     path("courses/",CourseListView.as_view(), name="courses_list_view"),

# ]
# urlpatterns = [
#     path("teachers/",TeacherListView.as_view(), name="teachers_list_view"),
# ]