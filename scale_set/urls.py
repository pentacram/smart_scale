from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import url


urlpatterns = [
    path('', HomeView, name='home'),
    # path('', UpdateView, name='index'),
    # path('', IndexView, name='index'),
    path('login/', LoginView, name='login'),
    path('logout', LogOutView, name="logout"),
    path('', TableView, name="table"),
    path('edit/<int:pk>', EditView, name="edit"),
    path('table/<int:id>/', AverageView, name="average"),
    path('delete/<int:id>', DeleteView, name="delete"),
    # path('alldata/<int:id>/$m=month', AllDataView, name='all-data'),
    path('alldata/<int:id>/<str:month>', AllDataView,name='all-data'),

]
