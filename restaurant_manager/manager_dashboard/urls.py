from django.urls import path,include
from . import views
#from staff import views
from staff import urls as staff_urls






app_name = 'manager_dashboard' 

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('staff/', include(staff_urls))
    #path('staff-list/', include("staff.urls",namespace="staff")),
   
    #path('staff_menu_items/', StaffMenuItemListCreateView.as_view(), name='staff_menu_items'),
     #path('menu/', views.menu, name='menu'),
    #path('menus/', views.menus_view, name='menus'),
   # path('link_staff/', 

]
