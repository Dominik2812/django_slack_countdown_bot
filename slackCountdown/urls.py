
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.start, name="start"),
    # path('error', views.error_view, name="error"),
    path('delete/<int:pk>', views.delete_countdown, name="delete_countdown")
]
