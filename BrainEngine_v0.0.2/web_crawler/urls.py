from django.conf.urls import url
from . import views

app_name = 'web_crawler'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
