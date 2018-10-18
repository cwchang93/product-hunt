
from django.urls import path, include
from . import views
#從當前目錄中引入views.py

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
]
