from django.conf.urls import url
from mlm import views

urlpatterns = [
    url(r'^home/$', views.home, name = 'home' ),
]