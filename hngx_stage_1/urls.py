from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:user_id>", views.update_user, name="update_user"),
    path("<str:username>", views.view_user, name="view_user"),
]
