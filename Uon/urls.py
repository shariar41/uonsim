"""
Definition of urls for Uon.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.student, name='student'),
    path('studentgrade/', views.studentGrades, name='student_grade'),
    path('transcript/', views.studentTranscript, name='student_transcript'),
    path('policy/', views.policy, name='policy'),
    path('profile/', views.profile, name='student_profile'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout',views.logout, name='logout'), #LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
