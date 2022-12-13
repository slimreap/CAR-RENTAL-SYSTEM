from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('listcars/', views.listcars, name = "listcars"),
    path('bookdetails/<int:id>', views.bookdetails, name = "bookdetails"),
    path('receipt/<int:id>', views.receipt, name = "receipt"),
    path(r'receipt/(?P<id>.*)/$', views.initialreceipt, name = "initialreceipt"),
    path('about/', views.about, name = "about"),
    path('adminview/', views.adminview, name="adminview" ),
    path('login/', views.loginPage, name="login" ),
    path('logout/', views.logoutUser, name="logout" ),
    path('register/', views.register, name="register" ),
    path('newupdate/<int:id>', views.newupdate, name="newupdate"),
    path('delete/<int:id>', views.delete, name = "delete"),
    path('confirm/<int:id>', views.confirm, name = "confirm"),
    path('turnin/<int:id>', views.turnin, name = "turnin"),
]