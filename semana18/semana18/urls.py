from django.contrib import admin
from django.urls import path
from app1 import views as appv
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',appv.index),
    path('meds/',appv.list_med),
    path('add_med/',appv.add_med,name="add_med"),
]
