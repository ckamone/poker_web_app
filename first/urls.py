"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from . import views

from pywebio.platform.django import webio_view
from .pywebio_app1 import bmi
from pywebio.input import input, FLOAT
from pywebio.output import *


# `task_func` is PyWebIO task function
webio_view_func = webio_view(bmi)


urlpatterns = [
    path(r"tool", webio_view_func),
    path('', views.HomePageView.as_view(template_name='home/main.html')),
]
