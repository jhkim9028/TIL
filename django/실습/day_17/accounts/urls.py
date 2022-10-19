from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('index/', views.index, name="index"),
    path('logout/',views.logout, name="logout"),
    path('<int:accounts_pk>/',views.detail, name="detail"),
]
