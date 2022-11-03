from profiles import views
from django.urls import path

urlpatterns = [
    
    # configured the URL
    path('',views.index, name="homepage"),
    path('register',views.register, name="register")
]
