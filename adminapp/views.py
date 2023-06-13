from django.shortcuts import render
from django.views import View
from .models import Jobs

class Home(View):
    def get(self,request):
        qs=Jobs.objects.all()
        con_dic={'records':qs}
        return render(request,'display.html',context=con_dic)
# Create your views here.
