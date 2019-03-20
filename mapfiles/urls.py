from django.contrib import admin
from django.urls import include, path
from mapfiles.views import  MyView
from . import views


urlpatterns = [
    path('mine/', MyView.as_view(), name='my-view'),
    path('', views.index, name='index'),
    path('upload/',views.model_form_upload, name='model_form_upload')
]