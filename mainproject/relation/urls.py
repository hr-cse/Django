from django.conf.urls import url
from django.urls import path
from relation import views

app_name = 'relation'

urlpatterns = [
	# path('signup/',views.signup,name='signup'),
	# path('user_login/',views.user_login,name='user_login'),
	url(r'signup/$',views.signup,name='signup'),
	url(r'home/$',views.home,name='home'),
	url(r'login/$',views.login,name='login'),
	url(r'profile/$',views.profile,name='profile'),
	url(r'^user_login/$',views.user_login,name='user_login'),
]