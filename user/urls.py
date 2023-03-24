from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.login_view),
    path('reg/', views.register),
    path('', views.main),
    path('logout/', views.logout_view),
    path('reg/school/', views.reg_school),
    path('reg/school/add-students', views.add_students),
    path('get-id', views.get_random_code)
]