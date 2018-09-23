from django import forms
from relation.models import UserInfo

class NewUserForm(forms.ModelForm):
	class Meta():
		model = UserInfo
		fields = '__all__'