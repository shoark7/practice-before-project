from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'user'
urlpatterns = [
    path('logout/', views.log_out, name='logout'),
    path('login/', views.log_in, name='login'),
    path('signin/', views.sign_in, name='signin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
