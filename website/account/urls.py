from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('createadmin', views.createadmin, name="createadmin"),
    path('login/', views.login_view, name="login_view"),
    path('dashboardHO/', views.dashboardHO, name="dashboardHO"),
    path('dashboardDO/', views.dashboardDO, name="dashboardDO"),
    path('headoffice/', views.headoffice, name="headoffice"),
    path('districtoffice/', views.districtoffice, name="districtoffice"),
    path('branchlocation/', views.branchlocation, name="branchlocation"),
    path('addlocation/', views.addlocation, name="addlocation"),
    path('createuser/', views.createuser, name="createuser"),
]