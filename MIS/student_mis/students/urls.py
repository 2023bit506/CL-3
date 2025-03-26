# from django.urls import path
# from . import views

# # urlpatterns = [
# #     path('students/', views.student_list, name='student_list'),
# #     path('students/<int:req_no>/', views.student_detail, name='student_detail'),
# # ]

# urlpatterns = [
#     path('api/students/', views.student_list, name='student_list'),  # API Endpoint
#     path('', views.index, name='index'),  # HTML Page
# ]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Render the main HTML file (Frontend)
    path('students/', views.student_list, name='student_list'),  # API: Get all students
    path('students/<int:req_no>/', views.student_detail, name='student_detail'),  # API: Get a single student by ReqNo
    path('add-student/', views.add_student, name='add_student'),
]





