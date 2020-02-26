"""trial_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from trial_app import views
from trial_app import wine

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admission/',views.admission),
    path('registerUser/',views.registerUser),
    path('readUsers/',views.readUsers),
    path('delete/<id>',views.deleteUsers),
    path('edit/<id>',views.editUsers) ,
    path('updateUser/<id>',views.updateUser),
    path('wineTemplate',views.wineTemplate),
    path('winePrediction/',wine.winePrediction),
    path('changeStudentStatus/<student_id>/<student_status>',views.changeStudentStatus) 

]
