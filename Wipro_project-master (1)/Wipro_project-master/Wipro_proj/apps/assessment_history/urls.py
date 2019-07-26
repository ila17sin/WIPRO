from django.conf.urls import url
from . import views
app_name = 'assessment_history'
urlpatterns = [
    url(r'^$', views.index, name = "home"),
]
