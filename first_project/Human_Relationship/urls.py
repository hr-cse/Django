from django.conf.urls import url
from Human_Relationship import views

app_name = 'Human_Relationship'
urlpatterns = [
    url(r'^signuppage/$',views.signuppage,name = 'signup'),
    url(r'^formpage/$',views.form_name_view,name= 'form_name_view'),
]
