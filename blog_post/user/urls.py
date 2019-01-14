from django.urls import include, path

from . import views

app_name = 'user'
urlpatterns = [
    path('logout/', views.log_out, name='logout'),
    path('login/', views.log_in, name='login'),
    path('signin/', views.sign_in, name='signin'),
]
