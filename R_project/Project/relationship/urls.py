from django.conf.urls import url
from relationship import views

app_name = 'relationship'
urlpatterns = [
    url(r'^signuppage/$',views.signuppage,name = 'signup'),
]
