from learnmodelform import views
from django.conf.urls import url,include

app_name = 'learnmodelform'

urlpatterns = [
	url(r'^home/$',views.home,name='home'),
	url(r'^user/$',views.user,name='user'),
]