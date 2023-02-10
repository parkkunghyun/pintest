
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "accountapp"
# 127.0.0.1:8000/account/hello_world
# 저거 치기 빡세니까 accountapp:hello_world 랑 같음
urlpatterns = [
    path("hello_world/", views.hello_world, name="hello_world"),
]
