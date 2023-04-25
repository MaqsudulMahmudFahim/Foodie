
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="name"),
    path('contact/',views.contact_us, name="contact")
]
