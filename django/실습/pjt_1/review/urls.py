from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('index/',views.index, name="index"),
    path('create/',views.create, name="create"),
    path('new/',views.new, name="new"),
    path('detail/<int:pk_>',views.detail, name="detail"),
    path('edit/<int:pk__>',views.edit,name="edit"),
    path('update/<int:pk___>',views.update,name="update"),
    path('delete/<int:pk>',views.delete, name="delete"),
]
