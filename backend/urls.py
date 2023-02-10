from django.urls import path
from backend import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('registration/',views.register,name="registration"),
    path('db_admin/',views.db_admin,name="db_admin"),
    path('ad_login/',views.ad_login,name="ad_login"),
    path('category/',views.cat_input,name="cat_input"),
    path('db_cat/',views.db_cat,name="db_cat"),
    path('cat_display/',views.cat_show,name="cat_show"),
    path('edit_cat/<int:dataid>/',views.edit_cat,name="edit_cat"),
    path('c_edit/<int:dataid>/',views.c_edit,name="c_edit"),
    path('del_cat/<int:dataid>/',views.del_cat,name="del_cat"),
    path('item_show/',views.item_show,name="item_show"),
    path('db_item/',views.db_item,name="db_item"),
    path('items_data/',views.items_data,name="items_data"),
    path('del_item/<int:dataid>/',views.del_item,name="del_item"),
    path('item_edit/<int:dataid>/',views.item_edit,name="item_edit"),
    path('item_e/<int:dataid>/',views.item_e,name="item_e"),
    path('admin_display/',views.admin_display,name="admin_display"),
    path('e_admin/<int:dataid>/',views.e_admin,name="e_admin"),
    path('edit_admin/<int:dataid>/',views.edit_admin,name="edit_admin"),
    path('del_admin/<int:dataid>/',views.del_admin,name="del_admin"),
    path('contact_details/',views.contact_details,name="contact_details"),
    path('log_out/',views.log_out,name="log_out"),
    path('del_contact/<int:dataid>/',views.del_contact,name="del_contact"),
    
]