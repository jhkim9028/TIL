from django.urls import path
from . import views

app_name="articles"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/',views.create, name="create"),
    path('<int:articles_pk>/',views.detail, name="detail"),
    path('<int:pk>/update/', views.update, name="update"),
    path('<int:pk>/delete', views.delete, name="delete"),
    path('<int:comment_pk>/comments/',views.create_comment, name="create_comment"),
]
