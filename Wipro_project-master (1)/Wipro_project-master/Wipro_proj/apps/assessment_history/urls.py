from django.conf.urls import url
from . import views
app_name = 'assessment_history'
urlpatterns = [
    url(r'^$', views.index, name = "home"),
    url(r'^company/', views.company, name = "company"),
    url(r'^all/', views.all, name = "all")
    #url(r'^testing/', views.test, name = "testing")
]
