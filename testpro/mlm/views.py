from django.shortcuts import render
from mlm.models import UserTable


# Create your views here.
def index(request):
    return render(request, "index.html")


def home(request):
    user_list = UserTable.objects.order_by('userName')
    date_dic = {'access_records': user_list}
    return render(request, 'home.html', context=date_dic)
