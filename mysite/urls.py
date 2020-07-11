"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from base.views import home
from base.views import set_entrada
from nrzl.views import nrzl_view
from nrzi.views import nrzi_view
from ami.views import ami_view
from pseudoternario.views import pseudoternario_view
from manchester.views import manchester_view
from manchester_diferencial.views import manchester_diferencial_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('nrzl/<entrada>', nrzl_view, name="nrzl"),
    path('nrzi/<entrada>', nrzi_view, name="nrzi"),
    path('ami/<entrada>', ami_view, name="ami"),
    path('pseudoternario/<entrada>', pseudoternario_view, name="pseudoternario"),
    path('manchester/<entrada>', manchester_view, name="manchester"),
    path('manchester_diferencial/<entrada>', manchester_diferencial_view, name="manchester_diferencial"),
    path('set-entrada', set_entrada),

]
