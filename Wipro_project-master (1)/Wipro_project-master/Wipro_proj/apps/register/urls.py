from django.conf.urls import url
from . import views
app_name = 'register'
urlpatterns = [
    url(r'^$', views.index, name = "home"),
    url(r'^register/', views.register, name = "register"),
    url(r'^login/', views.login, name = "login"),
    url(r'^loginhome/', views.loginindex, name = "loginhome"),
    url(r'^logout/', views.logout, name = "logout")
]
