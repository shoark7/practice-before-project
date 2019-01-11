from django.urls import path

from . import views


app_name = 'post'
urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    # path('', views.post_list, name='list'),
    path('<int:pk>', views.PostDetail.as_view(), name='detail'),
    # path('<int:post_id>', views.post_detail, name='detail'),
]
