from django.urls import path

from . import views


app_name = 'post'
urlpatterns = [
    path('new/', views.new_page, name="new"),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
]
