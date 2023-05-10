from django.contrib import admin
from django.urls import path, include





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('manager_dashboard/', include(('manager_dashboard.urls','manager_dashboard'), namespace='manager_dashboard')),
    path('staff/', include('staff.urls')),
   # path('resto/', include('resto.urls')),
    #path('restaurant/', include('restaurant.urls')),
    
]





# project/urls.py
#from django.urls import path, include

#urlpatterns = [
#path('api/', include('restaurant.urls')),
#]
