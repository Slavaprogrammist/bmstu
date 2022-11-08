from django.contrib import admin
from bmstu_lab import views as cars_views
from bmstu_lab import views as user_views
from bmstu_lab import views as arenda_views
from bmstu_lab import views as tx_views
from django.urls import include, path
from rest_framework import routers
from bmstu_lab import views

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.AllGuests),
    #path('guest/<int:id>/', views.GetGuest, name='guest_url'),
    path('', views.carList),
    path('car/<int:id>/', views.Getcars, name='cars_url'),
    #path('showall/', views.accommodationList),
    #path('admin/', admin.site.urls),
    #path('', views.GetOrders),
    #path('order/<int:id>/', views.GetOrder, name='order_url'),
]"""


router = routers.DefaultRouter()
router.register(r'cars', cars_views.CarsViewSet)
router.register(r'user', user_views.UserViewSet)
router.register(r'arenda', arenda_views.ArendaViewSet)
router.register(r'tx', tx_views.TxViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]

