from django.conf.urls import url
from relation import views

app_name = 'relation'
urlpatterns = [
    url(r'^home/$',views.home,name = 'home'),
    url(r'^user/$',views.user,name= 'user'),
]