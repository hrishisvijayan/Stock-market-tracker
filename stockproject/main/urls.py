from . import views
from django.urls import path

urlpatterns = [
    path('',views.stockPicker,name='stockpicker'),
]