from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path('signup/',views.signup, name="signup"),
    path('<int:accounts_pk>/',views.detail, name="detail"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('update/',views.update, name="update"),
]

