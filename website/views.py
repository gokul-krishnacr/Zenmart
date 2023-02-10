from django.shortcuts import render,redirect
from backend.models import cat_db,item_db,contact_db
from website.models import reg_db
from django.contrib.auth import authenticate,logout
from django.contrib import messages

# Create your views here.

def index(request):
    data=cat_db.objects.all()
    return render(request,'home.html',{"data":data})

def product_data(req):
    data=cat_db.objects.all()
    daca=item_db.objects.all()
    return render(req,'products.html',{"data":data,"daca":daca})

def dis_cat(request,itemCatg):
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    items=item_db.objects.filter(category=itemCatg)
    data=cat_db.objects.all()
    context={
        'items':items,
        'catg':catg,
        'data':data
    }
    return render(request,"cat_dis.html",context)

def pro_details(request,dataid):
    data=cat_db.objects.all()
    dat=item_db.objects.get(id=dataid)
    return render(request,'product_details.html',{"data":data,"dat":dat})

def login_(request):
    return render(request,'login_form.html')

def reg(request):
    return render(request,'register_form.html')

def regdb(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        em=request.POST.get('email')
        ps=request.POST.get('password')
        rps=request.POST.get('r_password')
        mb=request.POST.get('mobile')
        if ps==rps:
            obj=reg_db(name=nm,email=em,password=ps,r_password=rps)
            obj.save()
            return redirect(login_)
        else:
            # context={
            #     'msg:"Sorry... password not matched'
            # }
            return render(request,'registr_form.html')

def log_user(request):
    if request.method=="POST":
        u=request.POST.get('name')
        p=request.POST.get('password')
        if reg_db.objects.filter(name=u,password=p).exists():
            request.session['name']=u
            request.session['password']=p
            return redirect(index)
        else:
            messages.error(request, 'Incorrect password')
            return redirect(login_)

def contact(request):
    data=cat_db.objects.all()
    return render(request,'contact_us.html',{"data":data})

def db_contact(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        nb=request.POST.get('number')
        em=request.POST.get('email')
        nd=request.POST.get('need')
        msg=request.POST.get('message')
        obj=contact_db(name=nm,number=nb,email=em,need=nd,message=msg)
        obj.save()
        return redirect(contact)

def logout_(request):
    logout(request)
    return redirect(login_)

def pay(request):
    return render(request,'payment.html')