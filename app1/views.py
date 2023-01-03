from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.
def registertion(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf,'pf':pf}
    if request.method=='POST' and request.FILES:
        ud=UserForm(request.POST)
        pd=ProfileForm(request.POST,request.FILES)
        if ud.is_valid() and pd.is_valid():
            pw=ud.cleaned_data['password']
            uso=ud.save(commit=False)
            uso.set_password(pw)
            uso.save()
            
            po=pd.save(commit=False)
            po.user=uso
            po.save()
            
            return HttpResponse('registering is done')
    return render(request,'registertion.html',d)