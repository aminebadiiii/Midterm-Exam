"""
URL configuration for concordiabooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.student_login, name='login'),
    path('register/', views.student_register, name='register'),
    path('add-textbook/', views.add_textbook, name='add_textbook'),
    path('my-textbooks/', views.my_textbooks, name='my_textbooks'),
    path('textbooks/<str:course_code>/', views.textbook_list_by_course, name='textbook_list_by_course'),
    path('delete-textbook/<int:textbook_id>/', views.delete_textbook, name='delete_textbook'),
    path('', views.home, name='home'),
    path('logout/', views.student_logout, name='logout'),
]
