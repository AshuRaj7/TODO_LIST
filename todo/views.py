from django.shortcuts import render,redirect
from .models import data
# Create your views here.
def index(request):
    todos =data.objects.all()
    if request.method=='POST':
        new =data(
            title= request.POST['title']
        )
        new.save()
        return redirect('/')
    return render(request,'index.html',{'todos':todos})