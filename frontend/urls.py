from django.urls import path
from frontend import views

urlpatterns = [
    path('h1/',views.h1,name="h1"),
    path('',views.index1,name="index1"),
    path('contact1/',views.contact1,name="contact1"),
    path('reg1/',views.reg1,name="reg1"),
    path('regdb1/',views.regdb1,name="regdb1"),
    path('login_1/',views.login_1,name="login_1"),
    path('log_user1/',views.log_user1,name="log_user1"),
    path('product_data1/',views.product_data1,name="product_data1"),
    path('pro_details1/<int:dataid>/',views.pro_details1,name="pro_details1"),
    path('dis_cat1/<itemCatg>/',views.dis_cat1,name="dis_cat1"),
    path('logout/',views.logout_1,name="logout_1"),
    path('db_contact1/',views.db_contact1,name="db_contact1"),
    path('pay1/',views.pay1,name="pay1"),
]