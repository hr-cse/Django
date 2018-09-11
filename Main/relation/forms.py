from django import forms
from relation.models import userInfo

class NewUserForm(forms.ModelForm):
	class Meta():
		model = userInfo
		fields = '__all__'