from django.shortcuts import render,redirect
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from UserApp . models import *
# Create your views here.
def index(request):
    addcate=AddCat.objects.all().count()
    addgro=AddMov.objects.all().count()
    addlo=Login.objects.all().count()
    addcont=Contact.objects.all().count()
    data11=Checkout.objects.all().count()
    
    return render(request,'index.html',{'data':addcate,'bata':addgro,'log':addlo,'contacting':addcont,'data4':data11})
def addcategory(request):
    return render(request,'addcategory.html')
def addgrocery(request):
    data3=AddCat.objects.all()
    return render(request,'addgrocery.html',{'data3':data3})
def firststep(request):
    return render(request,'addcategory.html')
def add_cat(request):
    if request.method=='POST':
       catname=request.POST['catname']
       catdescription=request.POST['catdescription']
       images=request.FILES['photoos']
    
       
       data=AddCat(catname=catname,catdescription=catdescription,images=images)
       data.save()
       return redirect('second_step')
def second_step(request):
       items=AddCat.objects.all()
       return render(request,'tablecategory.html',{'items':items})
def edit(request,id):
    data=AddCat.objects.filter(id=id)
    return render(request,'editcategory.html',{'data':data})
def update(request,id):
   if request.method=='POST':
       catname=request.POST['catname']
       catdescription=request.POST['catdescription']
       
       try:
            img_c = request.FILES['photoos']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
       except MultiValueDictKeyError:
            file = AddMov.objects.get(id=id).img
       
       AddCat.objects.filter(id=id).update(catname=catname,catdescription=catdescription,images=file)
       return redirect('second_step')
def delete(request,id):
    
       
       AddCat.objects.filter(id=id).delete()
       
       
       return redirect('second_step')
def thirdstep(request):
    
    return render(request,'addgrocery.html')
def add_mov(request):
    if request.method=='POST':
       moviename=request.POST['moviename']
       
       
       moviecategory=request.POST['moviecategory']
       movielang=request.POST['movielang']
       moviegenre=request.POST['moviegenre']
       price=request.POST['price']
       image=request.FILES['photos']
       
    
       
       bata=AddMov(moviename=moviename,image=image,moviecategory=moviecategory,movielang=movielang,moviegenre=moviegenre,price=price)
       bata.save()
       return redirect('fourth_step')
   
def fourth_step(request):
    data3=AddCat.objects.all()
    iitems=AddMov.objects.all()
    return render(request,'tablegrocery.html',{'bata':iitems,'data3':data3})
def edition(request,id):
    data3=AddCat.objects.all()
    datta=AddMov.objects.filter(id=id)
    return render(request,'editgrocery.html',{'bata':datta,'data3':data3})
def updation(request,id):
   if request.method=='POST':
       moviename=request.POST['moviename']
       
       
       moviecategory=request.POST['moviecategory']
       movielang=request.POST['movielang']
       moviegenre=request.POST['moviegenre']
       price=request.POST['price']
       
    
       try:
            img_c = request.FILES['photos']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
       except MultiValueDictKeyError:
            file = AddMov.objects.get(id=id).img
       
       AddMov.objects.filter(id=id).update(moviename=moviename,moviecategory=moviecategory, movielang= movielang,moviegenre=moviegenre,price=price,image=file)
       return redirect('fourth_step')
def deletion(request,id):
    
       
       AddMov.objects.filter(id=id).delete()
       
       
       return redirect('fourth_step') 
   
   
   
    
def product(request,id):
   if request.method=='POST':
       moviename=request.POST['moviename']
       
       
       moviecategory=request.POST['moviecategory']
       movielang=request.POST['movielang']
       moviegenre=request.POST['moviegenre']
       movieimage=request.FILES['movies']
       price=request.POST['price']
       data=AddMov(moviename=moviename,moviecategory=moviecategory,movielang= movielang,moviegenre=moviegenre,movieimage=movieimage,price=price)
       data.save()
       AddMov.objects.filter(id=id)
       return redirect('production')
def production(request):
    mata=AddMov.objects.all()
    return render(request,'viewgrocery.html',{'data':mata})
def nextproduct(request,id):
    cata=AddMov.objects.filter(id=id)
    return render(request,'singlegrocery.html',{'data':cata})

def contact_table(request):
    return render(request,'contact_table.html')



def substance(request,id):
   if request.method=='POST':
       
       catname=request.POST['catname']
       catdescription=request.POST['catdescription']
       images=request.FILES['moviess']
      
       data=AddMov(catname=catname,catdescription=catdescription,images=images)
       data.save()
       AddCat.objects.filter(id=id)
       return redirect('material')
def material(request):
    mata=AddCat.objects.all()
    return render(request,'viewcategory.html',{'data':mata})
def nextmaterial(request,id):
    cata=AddCat.objects.filter(id=id)
    return render(request,'singlecategory.html',{'data':cata})   



def regview(request):
    geeting=Login.objects.all()
    return render(request,'viewreguser.html',{'log':geeting})
def contactview(request):
    getting=Contact.objects.all()
    return render(request,'contact_table.html',{'contacting':getting})
def checkouttable(request):
    data11=Checkout.objects.all()
    
    
    return render(request,'checkouttable.html',{'data4':data11})