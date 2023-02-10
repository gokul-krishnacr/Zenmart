from django.urls import path
from website import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('products/',views.product_data,name="product_data"),
    path('dis_cat/<itemCatg>/',views.dis_cat,name="dis_cat"),
    path('pro_details/<int:dataid>/',views.pro_details,name="pro_details"),
    path('',views.login_,name="login_"),
    path('reg/',views.reg,name="reg"),
    path('regdb/',views.regdb,name="regdb"),
    path('log_user/',views.log_user,name="log_user"),
    path('contact/',views.contact,name="contact"),
    path('db_contact/',views.db_contact,name="db_contact"),
    path('logout/',views.logout_,name="logout_"),
    path('pay/',views.pay,name="pay")
]