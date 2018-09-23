from django import forms
from mlm.models import UserTable


class NewUserForm(forms.ModelForm):
    class Meta():
        model = UserTable
        fields = '__all__'
