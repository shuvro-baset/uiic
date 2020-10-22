from django.urls import path
from . import views

app_name = 'reg_app'
urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('', views.LogView.as_view(), name='log'),
    path('course-registration/', views.CourseRegView.as_view(), name='course_registration'),
    path('dashboard/<str:stu_id>', views.DashboardView.as_view(), name='dashboard'),
    path('forget-password', views.ForgetPass.as_view(), name='forget_pass'),
    path('reset-password', views.ResetPass.as_view(), name='reset_pass'),

]