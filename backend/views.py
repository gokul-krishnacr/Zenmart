from django.shortcuts import render,redirect
from backend.models import admin_db,cat_db,item_db,contact_db
from django.contrib.auth import authenticate,logout
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def home(request):
    return render(request,'index.html')

def register(req):
    return render(req,'registration.html')

def login(req):
    return render(req,'login.html')

def db_admin(request):
    if request.method=="POST":
        nm=request.POST.get('username')
        em=request.POST.get('email')
        ps=request.POST.get('password')
        rps=request.POST.get('r_password')
        mb=request.POST.get('mobile')
        if ps==rps:
            obj=admin_db(username=nm,email=em,password=ps,r_password=rps,mobile=mb)
            obj.save()
            return redirect(login)
        else:
            return redirect(register)
        

# def ad_login(request):
#     if request.method=="POST":
#         u_name=request.POST.get('username')
#         ps=request.POST.get('password')

#         if admin_db.objects.filter(username__contains=u_name).exists():
#             user=authenticate(username=u_name,password=ps)
#             if user is not None:
#                 login(request,user)
#                 request.session['username']=u_name
#                 request.session['password']=ps
#                 return redirect(request,'index.html')
#             else:
#                 return redirect(login_f)
#         else:
#             return redirect(login_f)

def ad_login(request):
    if request.method=="POST":
        u=request.POST.get('username')
        p=request.POST.get('password')
        if admin_db.objects.filter(username=u,password=p).exists():
            request.session['username']=u
            request.session['password']=p
            return redirect(home)
        else:
            return redirect(login,{"msg:invalid username or password"})

def cat_input(request):
    return render(request,'category.html')

def db_cat(request):
    if request.method=="POST":
        ct=request.POST.get('category')
        qt=request.POST.get('quality')
        img=request.FILES['image']
        obj=cat_db(category=ct,quality=qt,image=img)
        obj.save()
        return redirect(cat_input)

def cat_show(request):
    data=cat_db.objects.all()
    return render(request,'cat_display.html',{"data":data})

def del_cat(request,dataid):
    data=cat_db.objects.get(id=dataid)
    data.delete()
    return redirect(cat_show)

def edit_cat(request,dataid):
    data=cat_db.objects.get(id=dataid)
    print(data)
    return render(request,'cat_edit.html',{"data":data})

def c_edit(request,dataid):
    if request.method=="POST":
        ct=request.POST.get('category')
        qt=request.POST.get('quality')
        try:
            im=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name, im)
        except MultiValueDictKeyError:
            file=cat_db.objects.get(id=dataid).image
        cat_db.objects.filter(id=dataid).update(category=ct,quality=qt,image=file)
        return redirect(cat_show)

def item_show(request):
    data=cat_db.objects.all()
    return render(request,'items.html',{"data":data})

def db_item(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        pr=request.POST.get('price')
        ct=request.POST.get('category')
        sz=request.POST.get('size')
        im=request.FILES['image']
        obj=item_db(name=nm,price=pr,category=ct,size=sz,image=im)
        obj.save()
        return redirect(item_show)

def items_data(request):
    data=item_db.objects.all()
    return render(request,'item_display.html',{"data":data})

def item_e(request,dataid):
    data=item_db.objects.get(id=dataid)
    daca=cat_db.objects.all()
    print(data)
    return render(request,'edit_item.html',{"data":data,"daca":daca})

def del_item(request,dataid):
    data=item_db.objects.get(id=dataid)
    data.delete()
    return redirect(items_data)

def item_edit(request,dataid):
    if request.method=="POST":
        nm=request.POST.get('name')
        pr=request.POST.get('price')
        ct=request.POST.get('category')
        sz=request.POST.get('size')
        try:
            im=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name, im)
        except MultiValueDictKeyError:
            file=item_db.objects.get(id=dataid).image
        item_db.objects.filter(id=dataid).update(category=ct,name=nm,price=pr,size=sz,image=file)
        return redirect(items_data)

def admin_display(request):
    data=admin_db.objects.all()
    return render(request,'Admin_data.html',{"data":data})

def e_admin(request,dataid):
    data=admin_db.objects.get(id=dataid)
    return render(request,'admin_edit.html',{"data":data})

def edit_admin(request,dataid):
    if request.method=="POST":
        nm=request.POST.get('username')
        em=request.POST.get('email')
        ps=request.POST.get('password')
        rps=request.POST.get('r_password')
        mb=request.POST.get('mobile')
        admin_db.objects.filter(id=dataid).update(username=nm,email=em,password=ps,r_password=rps,mobile=mb)
        return redirect(admin_display)

def del_admin(request,dataid):
    data=admin_db.objects.get(id=dataid)
    data.delete()
    return redirect(admin_display)

def contact_details(request):
    data=contact_db.objects.all()
    return render(request,'contact_data.html',{"data":data})

def log_out(request):
    logout(request)
    return redirect(login)

def del_contact(request,dataid):
    data=contact_db.objects.get(id=dataid)
    data.delete()
    return redirect(contact_details)


