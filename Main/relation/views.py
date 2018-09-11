from django.shortcuts import render
# from django.http import HttpResponse
from relation.forms import NewUserForm
# from relation.models import userInfo

# Create your views here.
def index(request):
	return render(request,'index.html')

def home(request):
	return render(request,'home.html')

def user(request):
	form = NewUserForm()

	if request.method == 'POST':
		form = NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print("ERROR!")
	return render(request,'user.html',{'form':form})





# def b_user(request):
# 	user_list = userInfo.objects.order_by('firstName')
# 	user_dic = {'users':user_list}
# 	return render(request,'user.html',context=user_dic)
