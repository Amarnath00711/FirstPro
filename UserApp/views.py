from django.shortcuts import render,redirect
from . models import *
from AdminApp . models import *
from django.db.models.aggregates import Sum
# Create your views here.
def indexuser(request):
    job=AddCat.objects.all()
    data1=AddMov.objects.all()
    a=request.session.get('u_id')
    data3=Cart.objects.filter(userid=a,status=0).count()
    
    
    return render(request,'indexuser.html',{'data':job,'data1':data1,'data3':data3})
def viewcategory(request):
    return render(request,'viewcategory.html')
def viewgrocery(request):
    return render(request,'viewgrocery.html')
def singlecategory(request):
    return render(request,'singlecategory.html')
def singlegrocery(request):
    return render(request,'singlegrocery.html')
def contact(request):
    return render(request,'contact.html')
def contactfrom(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        
        contacting=Contact(name=name,email=email,subject=subject,message=message)
        contacting.save()
        
    return redirect('contact')

def contactview(request):
    getting=Contact.objects.all()
    return render(request,'contact_table.html',{'contacting':getting})
def editing(request,id):
    data=Contact.objects.filter(id=id)
    return render(request,'edit_contact.html',{'contacting':data})
def updating(request,id):
   if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['messsage']
       
        Contact.objects.filter(id=id).update(name=name,email=email,subject=subject,message=message)
        return redirect('contactview')
def deleting(request,id):
    
       
       Contact.objects.filter(id=id).delete()
       
       
       return redirect('contactview') 
   
def signin(request):
    return render(request,'signin.html')
def login(request):
    return render(request,'login.html')
def loginusing(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        phone=request.POST['phone']
        log=Login(username=username,password=password,email=email,phone=phone)
        log.save()
        
        return redirect('login')
def userdata(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Login.objects.filter(username=username,password=password).exists():
            data=Login.objects.filter(username=username,password=password).values('email','phone' ,'id').first()
           
            request.session['email_u'] = data['email']
            request.session['phonenumber_u'] = data['phone']
            request.session['u_id'] = data['id']
             
             
            request.session['username_u'] = username
            request.session['password_u'] = password
            return redirect('categories') 
        else:
            return render(request,'login.html',{'msg':"invalid user credentials"})
    else:
        return redirect('login')      
def userlogout(request):
    del request.session['username_u']
    del request.session['password_u']
    del request.session['email_u']
    del request.session['phonenumber_u']
    del request.session['u_id']
    
    
    
    
    return redirect('login')  



def category(request,id):
    if request.method=='POST':
       catname=request.POST['catname']
       catdescription=request.POST['catdescription']
    
       
       data=AddCat(catname=catname,catdescription=catdescription)
       data.save()
       AddCat.objects.filter(id=id)
       
    return redirect(request,'categories')
def categories(request):
    a=request.session.get('u_id')
    data3=Cart.objects.filter(userid=a,status=0).count()
    mata=AddCat.objects.all()
    return render(request,'viewcategory.html',{'data':mata,'data3':data3})  
def singleecategory(request,id):
    cata=AddCat.objects.filter(id=id)
    return render(request,'singlecategory.html',{'data':cata})




def shooting(request,id):
    if request.method=='POST':
       moviename=request.POST['moviename']
       
       
       moviecategory=request.POST['moviecategory']
       movielang=request.POST['movielang']
       moviegenre=request.POST['moviegenre']
       image=request.FILES['photos']
       
    
       
       bata=AddMov(moviename=moviename,image=image,moviecategory=moviecategory,movielang=movielang,moviegenre=moviegenre)
       bata.save()
       AddMov.objects.filter(id=id)
def cinema(request,category):
    if(category == "all"):
        data1 = AddMov.objects.all()
    else:
        data1= AddMov.objects.filter(moviecategory=category)  
    data2=AddCat.objects.all()
    
    a=request.session.get('u_id')
    data3=Cart.objects.filter(userid=a,status=0).count()
    return render(request,'viewgrocery.html',{'data1':data1,'data2':data2,'data3':data3})  
def singlemovie(request,id):
    smart=AddMov.objects.filter(id=id)
    a=request.session.get('u_id')
    data3=Cart.objects.filter(userid=a,status=0).count()
    return render(request,'singlegrocery.html',{'bata':smart,'data3':data3})  
def about(request):
    a=request.session.get('u_id')
    data3=Cart.objects.filter(userid=a,status=0).count()
    return render(request,'about.html',{'data3':data3})
def shopingcart(request):
    return render(request,'shopingcart.html')
def checkout(request):
    a=request.session.get('u_id')
    data3=Cart.objects.filter(userid=a,status=0).count()
    s=Cart.objects.filter(userid=a,status=0).aggregate(Sum('total'))
    data5=Cart.objects.filter(userid=a,status=0)
    return render(request,'checkout.html',{'data3':data3,'s':s,'data5':data5})
def checkoutinfo(request):
    if request.method=="POST":
        user_id=request.session.get('u_id')
        country2=request.POST['country']
        address2=request.POST['address']
        city2=request.POST['city']
        zip2=request.POST['zip']
        order=Cart.objects.filter(userid=user_id,status=0)
        
        for i in order:
            data4=Checkout(userid=Login.objects.get(id=user_id),cartid=Cart.objects.get(id=i.id),country=country2,address=address2,city=city2,zip=zip2)
            data4.save()
            Cart.objects.filter(id=i.id).update(status=1)
    return redirect('thankspage')        

def cart(request):
    a=request.session.get('u_id')
    data=Cart.objects.filter(userid=a,status=0)
    s=Cart.objects.filter(userid=a,status=0).aggregate(Sum('total'))
    a=request.session.get('u_id')
    data3=Cart.objects.filter(userid=a,status=0).count()
    return render(request,'shopingcart.html',{'data':data,'data3':data3,'s':s})
def cartdata(request,id):
    if request.method=="POST":
        user_id=request.session.get('u_id')
        quantity1=request.POST['quantity']
        total1=request.POST['total']
        
        data=Cart(userid=Login.objects.get(id=user_id),productid=AddMov.objects.get(id=id),quantity=quantity1,total=total1)
        data.save()
    return redirect('cart')    
def grocerystep(request):
    return render(request,'singlegrocery.html')
def add_gro(request):
    if request.method=='POST':
        user_id=request.session.get('u_id')
        quantity1=request.POST['quantity']
        total1=request.POST['total']
        data=Cart(userid=Login.objects.get(id=user_id),productid=AddMov.objects.get(id=id),quantity=quantity1,total=total1)
        data.save()
        return redirect('gro_step')
def gro_step(request):
    ittems=Cart.objects.all()
    return render(request,'shopingcart.html',{'ittems':ittems}) 
# def editt(request,id):
#     daaata=Cart.objects.filter(id=id)
#     return render(request,'editsinglegro.html',{'daaata':daaata})  
# def updaate(request,id):
#     if request.method=='POST':
#         user_id=request.session.get('u_id')
#         quantity1=request.POST['quantity']
#         total1=request.POST['total']
#     Cart.objects.filter(id=id).update(userid=Login.objects.get(id=user_id),productid=AddMov.objects.get(id=id),quantity=quantity1,total=total1)
#     return redirect('gro_step')
def deletee(request,id):
    Cart.objects.filter(id=id).delete()   
    
    return redirect('cart')
def thankspage(request):
    a=request.session.get('u_id')
    data3=Cart.objects.filter(userid=a,status=0).count()
    return render(request,'thankspage.html',{'data3':data3})
      