from django.shortcuts import render, redirect  
from CRUDAPP.forms import kullaniciForm  
from CRUDAPP.models import kullanici 
 
# Create your views here.  
def addnew(request):  
    if request.method == "POST":  
        form = kullaniciForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = kullaniciForm()  
    return render(request,'index.html',{'form':form})  
 
def index(request):  
    kullanicilar = kullanici.objects.all()  
    return render(request,"show.html",{'kullanicilar':kullanicilar})  
 
def edit(request, id):  
    Kullanici = kullanici.objects.get(id=id)  
    return render(request,'edit.html', {'kullanici':Kullanici})  
 
def update(request, id):  
    kullanicilar = kullanici.objects.get(id=id)  
    form = kullaniciForm(request.POST, instance = kullanicilar)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'kullanici': kullanicilar})  
     
def destroy(request, id):  
    Kullanici = kullanici.objects.get(id=id)  
    Kullanici.delete()  
    return redirect("/")
