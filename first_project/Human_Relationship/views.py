from django.shortcuts import render
from django.http import HttpResponse
from Human_Relationship.models import Topic,Webpage,AccessRecord
from . import forms

# Create your views here.

def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dic = {'access_records':webpages_list}
	return render(request,'index.html',context=date_dic)

def signuppage(request):
    return render(request,'signuppage.html')

def form_name_view(request):
	form = forms.FormName()

	if request.method == 'POST':
		form = forms.FormName(request.POST)

		if form.is_valid():
			print("OK")
			print("Name:"+form.cleaned_data['name'])
			print("Email:"+form.cleaned_data['email'])
			print("Text:"+form.cleaned_data['text'])

	return render(request,'form_page.html',{'form':form})
	# return render(request,'form_page.html')