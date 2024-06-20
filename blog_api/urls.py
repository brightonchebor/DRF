from django.urls import path
from .views import PostlList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    # path('', PostlList.as_view(), name='listcreate'),
]

