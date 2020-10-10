from django.urls import path
from . import views

app_name = 'reg_app'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LogView.as_view(), name='login'),
    path('course-registration/', views.CourseRegView.as_view(), name='course_registration'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

]