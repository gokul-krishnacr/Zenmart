from django.shortcuts import render,redirect
from backend.models import cat_db,item_db,contact_db
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from frontend.models import reg_db1

# Create your views here.
def h1(req):
    return render(req,'hello.html')

def index1(request):
    data=cat_db.objects.all()
    return render(request,'home1.html',{"data":data})

def contact1(request):
    data=cat_db.objects.all()
    return render(request,'contactus.html',{"data":data})

def login_1(request):
    return render(request,'logform.html')

def reg1(request):
    return render(request,'regform.html')

def regdb1(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        em=request.POST.get('email')
        ps=request.POST.get('password')
        rps=request.POST.get('r_password')
        mb=request.POST.get('mobile')
        if ps==rps:
            obj=reg_db1(name=nm,email=em,password=ps,r_password=rps)
            obj.save()
            return redirect(login_1)
        else:
            # context={
            #     'msg:"Sorry... password not matched'
            # }
            return render(request,'regform.html')


def log_user1(request):
    if request.method=="POST":
        u=request.POST.get('name')
        p=request.POST.get('password')
        if reg_db1.objects.filter(name=u,password=p).exists():
            request.session['name']=u
            request.session['password']=p
            return redirect(index1)
        else:
            messages.error(request, 'Incorrect password')
            return redirect(login_1)

def product_data1(req):
    data=cat_db.objects.all()
    daca=item_db.objects.all()
    return render(req,'products1.html',{"data":data,"daca":daca})

def pro_details1(request,dataid):
    data=cat_db.objects.all()
    dat=item_db.objects.get(id=dataid)
    return render(request,'products_details1.html',{"data":data,"dat":dat})

def dis_cat1(request,itemCatg):
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    items=item_db.objects.filter(category=itemCatg)
    data=cat_db.objects.all()
    context={
        'items':items,
        'catg':catg,
        'data':data
    }
    return render(request,"cat_dis1.html",context)

def logout_1(request):
    logout(request)
    return redirect(login_1)

def db_contact1(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        nb=request.POST.get('number')
        em=request.POST.get('email')
        nd=request.POST.get('need')
        msg=request.POST.get('message')
        obj=contact_db(name=nm,number=nb,email=em,need=nd,message=msg)
        obj.save()
        return redirect(contact1)
    
def pay1(request):
    return render(request,'payment1.html')


